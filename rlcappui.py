# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools.ui'
#
# Created: Sat Nov  5 16:37:23 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(585, 140)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(585, 140))
        MainWindow.setMaximumSize(QtCore.QSize(585, 200))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.session_link = QtGui.QLabel(self.centralwidget)
        self.session_link.setEnabled(True)
        self.session_link.setGeometry(QtCore.QRect(0, 0, 585, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.session_link.setPalette(palette)
        self.session_link.setFrameShape(QtGui.QFrame.NoFrame)
        self.session_link.setText("")
        self.session_link.setAlignment(QtCore.Qt.AlignCenter)
        self.session_link.setOpenExternalLinks(True)
        self.session_link.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.session_link.setObjectName("session_link")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(64, 64))
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionF1 = QtGui.QAction(MainWindow)
        self.actionF1.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("f1-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionF1.setIcon(icon)
        self.actionF1.setObjectName("actionF1")
        self.actionAC = QtGui.QAction(MainWindow)
        self.actionAC.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assetto_corsa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAC.setIcon(icon1)
        self.actionAC.setObjectName("actionAC")
        self.actionPCars = QtGui.QAction(MainWindow)
        self.actionPCars.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("project_cars.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPCars.setIcon(icon2)
        self.actionPCars.setObjectName("actionPCars")
        self.actionRF2 = QtGui.QAction(MainWindow)
        self.actionRF2.setCheckable(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("rfactor_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRF2.setIcon(icon3)
        self.actionRF2.setObjectName("actionRF2")
        self.actioniRacing = QtGui.QAction(MainWindow)
        self.actioniRacing.setCheckable(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("iracing_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actioniRacing.setIcon(icon4)
        self.actioniRacing.setObjectName("actioniRacing")
        self.actionSettings = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("settings-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon5)
        self.actionSettings.setObjectName("actionSettings")
        self.actionLog = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("log_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLog.setIcon(icon6)
        self.actionLog.setObjectName("actionLog")
        self.actionExit = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon7)
        self.actionExit.setObjectName("actionExit")
        self.toolBar.addAction(self.actionF1)
        self.toolBar.addAction(self.actionAC)
        self.toolBar.addAction(self.actionPCars)
        self.toolBar.addAction(self.actionRF2)
        self.toolBar.addAction(self.actioniRacing)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSettings)
        self.toolBar.addAction(self.actionLog)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionF1.setText(QtGui.QApplication.translate("MainWindow", "F1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionF1.setToolTip(QtGui.QApplication.translate("MainWindow", "Enable F1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAC.setText(QtGui.QApplication.translate("MainWindow", "AC", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAC.setToolTip(QtGui.QApplication.translate("MainWindow", "Enable Assetto Corsa", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPCars.setText(QtGui.QApplication.translate("MainWindow", "PCars", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPCars.setToolTip(QtGui.QApplication.translate("MainWindow", "Enable Project Cars", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRF2.setText(QtGui.QApplication.translate("MainWindow", "RF2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRF2.setToolTip(QtGui.QApplication.translate("MainWindow", "Enable RFactor2", None, QtGui.QApplication.UnicodeUTF8))
        self.actioniRacing.setText(QtGui.QApplication.translate("MainWindow", "iRacing", None, QtGui.QApplication.UnicodeUTF8))
        self.actioniRacing.setToolTip(QtGui.QApplication.translate("MainWindow", "Enable iRacing", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setToolTip(QtGui.QApplication.translate("MainWindow", "Show Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLog.setText(QtGui.QApplication.translate("MainWindow", "Log", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLog.setToolTip(QtGui.QApplication.translate("MainWindow", "Show log", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setToolTip(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))

