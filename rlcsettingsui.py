# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Mon Nov 14 11:33:00 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(550, 280)
        self.buttonBox = QtGui.QDialogButtonBox(Settings)
        self.buttonBox.setGeometry(QtCore.QRect(380, 245, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtGui.QTabWidget(Settings)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(5, 5, 541, 241))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 521, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.auth_code = QtGui.QLineEdit(self.groupBox_2)
        self.auth_code.setGeometry(QtCore.QRect(70, 20, 441, 20))
        self.auth_code.setObjectName("auth_code")
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 51, 20))
        self.label.setObjectName("label")
        self.driver_list = QtGui.QComboBox(self.groupBox_2)
        self.driver_list.setGeometry(QtCore.QRect(70, 50, 441, 22))
        self.driver_list.setObjectName("driver_list")
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 47, 20))
        self.label_2.setObjectName("label_2")
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 100, 251, 110))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 47, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 47, 20))
        self.label_4.setObjectName("label_4")
        self.forwarding_host = QtGui.QLineEdit(self.groupBox_3)
        self.forwarding_host.setGeometry(QtCore.QRect(50, 20, 160, 20))
        self.forwarding_host.setObjectName("forwarding_host")
        self.forwarding_port = QtGui.QLineEdit(self.groupBox_3)
        self.forwarding_port.setGeometry(QtCore.QRect(50, 50, 160, 20))
        self.forwarding_port.setObjectName("forwarding_port")
        self.forwarding_enable = QtGui.QCheckBox(self.groupBox_3)
        self.forwarding_enable.setGeometry(QtCore.QRect(50, 80, 160, 17))
        self.forwarding_enable.setObjectName("forwarding_enable")
        self.local_mode_box = QtGui.QGroupBox(self.tab)
        self.local_mode_box.setGeometry(QtCore.QRect(269, 100, 261, 110))
        self.local_mode_box.setObjectName("local_mode_box")
        self.local_mode = QtGui.QPushButton(self.local_mode_box)
        self.local_mode.setGeometry(QtCore.QRect(10, 20, 241, 30))
        self.local_mode.setObjectName("local_mode")
        self.label_6 = QtGui.QLabel(self.local_mode_box)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 241, 40))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab, "")
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.telemetry_enable = QtGui.QCheckBox(self.tab_6)
        self.telemetry_enable.setGeometry(QtCore.QRect(10, 10, 140, 30))
        self.telemetry_enable.setObjectName("telemetry_enable")
        self.label_7 = QtGui.QLabel(self.tab_6)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 100, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtGui.QLabel(self.tab_6)
        self.label_8.setGeometry(QtCore.QRect(10, 130, 100, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtGui.QLabel(self.tab_6)
        self.label_9.setGeometry(QtCore.QRect(10, 90, 100, 20))
        self.label_9.setObjectName("label_9")
        self.center_value = QtGui.QComboBox(self.tab_6)
        self.center_value.setGeometry(QtCore.QRect(119, 50, 410, 22))
        self.center_value.setObjectName("center_value")
        self.center_value.addItem("")
        self.center_value.addItem("")
        self.center_value.addItem("")
        self.bottom_left_value = QtGui.QComboBox(self.tab_6)
        self.bottom_left_value.setGeometry(QtCore.QRect(120, 90, 410, 20))
        self.bottom_left_value.setObjectName("bottom_left_value")
        self.bottom_left_value.addItem("")
        self.bottom_left_value.addItem("")
        self.bottom_left_value.addItem("")
        self.bottom_right_value = QtGui.QComboBox(self.tab_6)
        self.bottom_right_value.setGeometry(QtCore.QRect(120, 130, 410, 22))
        self.bottom_right_value.setObjectName("bottom_right_value")
        self.bottom_right_value.addItem("")
        self.bottom_right_value.addItem("")
        self.bottom_right_value.addItem("")
        self.diff_value = QtGui.QComboBox(self.tab_6)
        self.diff_value.setGeometry(QtCore.QRect(120, 170, 410, 22))
        self.diff_value.setObjectName("diff_value")
        self.diff_value.addItem("")
        self.diff_value.addItem("")
        self.label_11 = QtGui.QLabel(self.tab_6)
        self.label_11.setGeometry(QtCore.QRect(10, 170, 100, 20))
        self.label_11.setObjectName("label_11")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 521, 191))
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.f1_2016 = QtGui.QPushButton(self.groupBox)
        self.f1_2016.setGeometry(QtCore.QRect(265, 20, 245, 30))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.f1_2016.setFont(font)
        self.f1_2016.setObjectName("f1_2016")
        self.f1_2015 = QtGui.QPushButton(self.groupBox)
        self.f1_2015.setGeometry(QtCore.QRect(10, 20, 245, 30))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.f1_2015.setFont(font)
        self.f1_2015.setObjectName("f1_2015")
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 59, 500, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.rf2_install = QtGui.QPushButton(self.tab_3)
        self.rf2_install.setGeometry(QtCore.QRect(10, 10, 521, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.rf2_install.setFont(font)
        self.rf2_install.setObjectName("rf2_install")
        self.label_5 = QtGui.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 511, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget.addTab(self.tab_7, "")

        self.retranslateUi(Settings)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Settings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Settings.reject)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QtGui.QApplication.translate("Settings", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Settings", "Website Details", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Settings", "Auth Code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Settings", "Driver", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Settings", "Forwarding", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Settings", "Host", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Settings", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.forwarding_enable.setText(QtGui.QApplication.translate("Settings", "Enable", None, QtGui.QApplication.UnicodeUTF8))
        self.local_mode_box.setTitle(QtGui.QApplication.translate("Settings", "Local Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.local_mode.setText(QtGui.QApplication.translate("Settings", "Enable", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Settings", "Local mode disables the sending of lap and session data to the RLC website", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Settings", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.telemetry_enable.setText(QtGui.QApplication.translate("Settings", "Show Telemetry Window", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Settings", "Center Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Settings", "Bottom Right Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Settings", "Bottom Left Value", None, QtGui.QApplication.UnicodeUTF8))
        self.center_value.setItemText(0, QtGui.QApplication.translate("Settings", "Speed Delta", None, QtGui.QApplication.UnicodeUTF8))
        self.center_value.setItemText(1, QtGui.QApplication.translate("Settings", "Fuel Remaining", None, QtGui.QApplication.UnicodeUTF8))
        self.center_value.setItemText(2, QtGui.QApplication.translate("Settings", "Lap Delta", None, QtGui.QApplication.UnicodeUTF8))
        self.bottom_left_value.setItemText(0, QtGui.QApplication.translate("Settings", "Lap Delta", None, QtGui.QApplication.UnicodeUTF8))
        self.bottom_left_value.setItemText(1, QtGui.QApplication.translate("Settings", "Fuel Remaining", None, QtGui.QApplication.UnicodeUTF8))
        self.bottom_left_value.setItemText(2, QtGui.QApplication.translate("Settings", "Speed Delta", None, QtGui.QApplication.UnicodeUTF8))
        self.bottom_right_value.setItemText(0, QtGui.QApplication.translate("Settings", "Fuel Remaining", None, QtGui.QApplication.UnicodeUTF8))
        self.bottom_right_value.setItemText(1, QtGui.QApplication.translate("Settings", "Speed Delta", None, QtGui.QApplication.UnicodeUTF8))
        self.bottom_right_value.setItemText(2, QtGui.QApplication.translate("Settings", "Lap Delta", None, QtGui.QApplication.UnicodeUTF8))
        self.diff_value.setItemText(0, QtGui.QApplication.translate("Settings", "Last Lap", None, QtGui.QApplication.UnicodeUTF8))
        self.diff_value.setItemText(1, QtGui.QApplication.translate("Settings", "Best Lap", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Settings", "Difference based on", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QtGui.QApplication.translate("Settings", "Telemetry", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Settings", "Enable Telemetry", None, QtGui.QApplication.UnicodeUTF8))
        self.f1_2016.setText(QtGui.QApplication.translate("Settings", "F1 2016", None, QtGui.QApplication.UnicodeUTF8))
        self.f1_2015.setText(QtGui.QApplication.translate("Settings", "F1 2015", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Settings", "Click the above buttons to enable or disable the telemetry system for the respective game. If the location of the configuration file is unknown, you will be prompted to find it. The filename to select is called \'hardware_settings_config.xml\'.", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Settings", "CodeMasters F1", None, QtGui.QApplication.UnicodeUTF8))
        self.rf2_install.setText(QtGui.QApplication.translate("Settings", "Install", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Settings", "The above button will open a dialog box - please locate your rfactor2 installation directory. After this has been selected, a plugin will be installed that will allow this app to receive select telemetry data (speed, fuel, sector and lap times).", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("Settings", "rFactor2", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("Settings", "Assetto Corsa", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("Settings", "Project Cars", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QtGui.QApplication.translate("Settings", "iRacing", None, QtGui.QApplication.UnicodeUTF8))

