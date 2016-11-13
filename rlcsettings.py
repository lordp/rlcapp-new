from PySide import QtGui
import rlcsettingsui
import configparser
import functools
from rlcf1config import RLCF1Config


class RLCSettings(QtGui.QDialog, rlcsettingsui.Ui_Settings):
    def __init__(self, parent=None):
        super(RLCSettings, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle('Settings')

        self.tooltips = {}
        self.red_colour = QtGui.QPalette()
        self.red_colour.setColor(QtGui.QPalette.ButtonText, QtGui.QColor('#FF0000'))
        self.tooltips['disabled'] = 'Telemetry disabled'

        self.green_colour = QtGui.QPalette()
        self.green_colour.setColor(QtGui.QPalette.ButtonText, QtGui.QColor('#009900'))
        self.tooltips['enabled'] = 'Telemetry enabled'

        self.grey_colour = QtGui.QPalette()
        self.grey_colour.setColor(QtGui.QPalette.ButtonText, QtGui.QColor('#666666'))
        self.tooltips['unknown_config'] = 'Config file not found'

        self.local_mode.clicked.connect(self.toggle_local_mode)
        self.f1_2015.clicked.connect(functools.partial(self.find_f1_config, self.f1_2015))
        self.f1_2016.clicked.connect(functools.partial(self.find_f1_config, self.f1_2016))

        self.settings_path = 'config.ini'
        self.settings = configparser.ConfigParser()

        self.local_mode_enabled = False
        self.f1_2015_location = None
        self.f1_2015_enabled = False
        self.f1_2016_location = None
        self.f1_2016_enabled = False
        self.rf2_location = None

        self.initialise_settings()
        self.apply_settings()
        self.set_f1_button_colours()

    def find_f1_config(self, game):
        game_key = game.objectName()
        game_location = getattr(self, "{0}_location".format(game_key))

        config = RLCF1Config(game_key, game_location)
        config.toggle_telemetry()

        setattr(self, "{0}_location".format(game_key), config.config_file)
        setattr(self, "{0}_enabled".format(game_key), config.enabled())

        self.set_f1_button_colours()

    def set_f1_button_colours(self):
        if self.f1_2015_location == '':
            self.f1_2015.setPalette(self.grey_colour)
            self.f1_2015.setToolTip(self.tooltips['unknown_config'])
        else:
            if self.f1_2015_enabled:
                self.f1_2015.setPalette(self.green_colour)
                self.f1_2015.setToolTip(self.tooltips['enabled'])
            else:
                self.f1_2015.setPalette(self.red_colour)
                self.f1_2015.setToolTip(self.tooltips['disabled'])

        if self.f1_2016_location == '':
            self.f1_2016.setPalette(self.grey_colour)
            self.f1_2016.setToolTip(self.tooltips['unknown_config'])
        else:
            if self.f1_2016_enabled:
                self.f1_2016.setPalette(self.green_colour)
                self.f1_2016.setToolTip(self.tooltips['enabled'])
            else:
                self.f1_2016.setPalette(self.red_colour)
                self.f1_2016.setToolTip(self.tooltips['disabled'])

    def initialise_settings(self):
        self.settings['general'] = {}
        self.settings['telemetry'] = {}
        self.settings['f1_2015'] = {}
        self.settings['f1_2016'] = {}
        self.settings['rf2'] = {}
        self.settings['ac'] = {}
        self.settings['pcars'] = {}

        self.settings['general']['auth_code'] = ''
        self.settings['general']['driver'] = ''
        self.settings['general']['forwarding_host'] = ''
        self.settings['general']['forwarding_port'] = ''
        self.settings['general']['forwarding_enabled'] = 'False'
        self.settings['general']['local_mode'] = 'False'

        self.settings['telemetry']['enabled'] = 'False'
        self.settings['telemetry']['center_value'] = 'speed_delta'
        self.settings['telemetry']['bottom_left_value'] = 'lap_delta'
        self.settings['telemetry']['bottom_right_value'] = 'fuel'

        self.settings['f1_2015']['location'] = ''
        self.settings['f1_2015']['enabled'] = 'false'

        self.settings['f1_2016']['location'] = ''
        self.settings['f1_2016']['enabled'] = 'false'

        self.settings['rf2']['rf2_location'] = ''

        self.settings.read(self.settings_path)

    def save_settings(self):
        with open(self.settings_path, 'w') as settings:
            self.settings.write(settings)

    def apply_settings(self):
        self.auth_code.setText(self.settings['general']['auth_code'])
        self.set_combo_value(self.driver_list, self.settings['general']['driver'])
        self.forwarding_host.setText(self.settings['general']['forwarding_host'])
        self.forwarding_port.setText(self.settings['general']['forwarding_port'])
        self.forwarding_enable.setChecked(self.settings['general']['forwarding_enabled'] == 'True')

        self.local_mode_enabled = (self.settings['general']['local_mode'] == 'True')
        self.set_local_mode()

        self.telemetry_enable.setChecked(self.settings['telemetry']['enabled'] == 'True')
        self.set_combo_value(self.center_value, self.settings['telemetry']['center_value'])
        self.set_combo_value(self.bottom_left_value, self.settings['telemetry']['bottom_left_value'])
        self.set_combo_value(self.bottom_right_value, self.settings['telemetry']['bottom_right_value'])

        self.f1_2015_location = self.settings['f1_2015']['location']
        self.f1_2015_enabled = (self.settings['f1_2015']['enabled'] == 'true')

        self.f1_2016_location = self.settings['f1_2016']['location']
        self.f1_2016_enabled = (self.settings['f1_2016']['enabled'] == 'true')

        self.f1_2015.setPalette(self.red_colour if not self.f1_2015_enabled else self.green_colour)
        self.f1_2016.setPalette(self.red_colour if not self.f1_2016_enabled else self.green_colour)

        self.rf2_location = self.settings['rf2']['rf2_location']

    def set_combo_value(self, combo_box, value):
        index = combo_box.findText(value)
        if index > 0:
            combo_box.setCurrentIndex(index)

    def toggle_local_mode(self):
        self.local_mode_enabled = not self.local_mode_enabled
        self.set_local_mode()

    def set_local_mode(self):
        if self.local_mode_enabled:
            title = 'Local mode (enabled)'
            button = 'Disable'
        else:
            title = 'Local mode (disabled)'
            button = 'Enable'

        self.local_mode_box.setTitle(title)
        self.local_mode.setText(button)

    def accept(self):
        self.settings['general']['auth_code'] = self.auth_code.text()
        self.settings['general']['driver'] = self.driver_list.currentText()
        self.settings['general']['forwarding_host'] = self.forwarding_host.text()
        self.settings['general']['forwarding_port'] = self.forwarding_port.text()
        self.settings['general']['forwarding_enabled'] = str(self.forwarding_enable.isChecked())
        self.settings['general']['local_mode'] = str(self.local_mode_enabled)

        self.settings['telemetry']['enabled'] = str(self.telemetry_enable.isChecked())
        self.settings['telemetry']['center_value'] = self.center_value.currentText()
        self.settings['telemetry']['bottom_left_value'] = self.bottom_left_value.currentText()
        self.settings['telemetry']['bottom_right_value'] = self.bottom_right_value.currentText()

        self.settings['f1_2015']['location'] = self.f1_2015_location
        self.settings['f1_2015']['enabled'] = str(self.f1_2015_enabled).lower()

        self.settings['f1_2016']['location'] = self.f1_2016_location
        self.settings['f1_2016']['enabled'] = str(self.f1_2016_enabled).lower()

        self.settings['rf2']['rf2_location'] = self.rf2_location

        self.save_settings()

        super(RLCSettings, self).accept()

    def reject(self):
        super(RLCSettings, self).reject()
