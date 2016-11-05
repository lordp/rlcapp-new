import sys
from PySide import QtGui, QtCore
import rlcappui
from rlcsettings import RLCSettings
from rlcweb import RLCWeb
import rlcappicons


class RLCApp(QtGui.QMainWindow, rlcappui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(RLCApp, self).__init__(parent)
        self.setupUi(self)

        self.icons = {}
        self.set_icons()

        self.setWindowTitle('Racing League Charts Logger app')

        self.settings = RLCSettings(self)
        self.rlc_web = None
        self.telemetry_system = None

        self.actionF1.triggered[bool].connect(self.action_f1)

        self.actionSettings.triggered.connect(self.show_settings)
        self.actionExit.triggered.connect(self.action_exit)

        self.session_link.hide()
        self.timer = None

    def set_icons(self):
        self.icons['f1'] = QtGui.QIcon(':/icons/f1-icon.png')
        self.icons['ac'] = QtGui.QIcon(':/icons/assetto_corsa.png')
        self.icons['pcars'] = QtGui.QIcon(':/icons/project_cars.png')
        self.icons['rf2'] = QtGui.QIcon(':/icons/rfactor_2.png')
        self.icons['iracing'] = QtGui.QIcon(':/icons/iracing_logo.png')
        self.icons['log'] = QtGui.QIcon(':/icons/log_icon.png')
        self.icons['settings'] = QtGui.QIcon(':/icons/settings-icon.png')
        self.icons['exit'] = QtGui.QIcon(':/icons/exit.png')
        self.icons['app'] = QtGui.QIcon(':/icons/rlc.ico')

        self.actionF1.setIcon(self.icons['f1'])
        self.actionAC.setIcon(self.icons['ac'])
        self.actionPCars.setIcon(self.icons['pcars'])
        self.actionRF2.setIcon(self.icons['rf2'])
        self.actioniRacing.setIcon(self.icons['iracing'])
        self.actionLog.setIcon(self.icons['log'])
        self.actionSettings.setIcon(self.icons['settings'])
        self.actionExit.setIcon(self.icons['exit'])
        self.setWindowIcon(self.icons['app'])

    def create_web_interface(self):
        if self.settings.local_mode_enabled:
            token = self.settings.settings['general']['auth_code']
            driver = self.settings.settings['general']['driver']
            race = None

            self.rlc_web = RLCWeb(self, driver, race, token)

            self.timer = QtCore.QTimer()
            self.timer.setSingleShot(False)
            self.timer.timeout.connect(self.check_session_link)
            self.timer.start(500)

    def check_session_link(self):
        if self.rlc_web is not None and self.rlc_web.session_number > 0:
            self.session_link.setText(self.rlc_web.session_link)
            self.session_link.show()

    def show_telemetry_window(self):
        if self.settings.settings['telemetry']['enabled'] == 'True':
            from rlctelemetry import RLCTelemetry
            RLCTelemetry(self)

    def action_f1(self, checked=False):
        if checked:
            self.create_web_interface()
            self.show_telemetry_window()

            from rlcf1telemetry import RLCF1Telemetry
            self.telemetry_system = RLCF1Telemetry(self, self.rlc_web)
        else:
            self.timer.stop()
            if self.telemetry_system is not None:
                self.telemetry_system.close()
                self.telemetry_system = None

    def show_message(self, message):
        self.statusbar.showMessage(message, 2000)

    def show_settings(self):
        self.settings.setModal(True)
        self.settings.show()

    def action_exit(self):
        self.close()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = RLCApp()
    window.show()
    app.exec_()
