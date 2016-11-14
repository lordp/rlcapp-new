from PySide import QtGui, QtCore
import rlctelemetryui
from rlclap import RLCLap
import math


class RLCTelemetry(QtGui.QDialog, rlctelemetryui.Ui_Dialog):
    def __init__(self, settings):
        super(RLCTelemetry, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('Telemetry')
        self.setWindowIcon(QtGui.QIcon(':/icons/rlc.ico'))

        self.red_colour = QtGui.QPalette()
        self.red_colour.setColor(QtGui.QPalette.WindowText, QtGui.QColor('#FF0000'))

        self.green_colour = QtGui.QPalette()
        self.green_colour.setColor(QtGui.QPalette.WindowText, QtGui.QColor('#00FF00'))

        self.black_colour = QtGui.QPalette()
        self.black_colour.setColor(QtGui.QPalette.Window, QtGui.QColor('#000000'))
        self.setPalette(self.black_colour)

        self.settings = settings

        self.this_lap = {}
        self.compare_lap = {}

        self.speed_value = 0
        self.time_value = 0
        self.fuel_value = 0
        self.current_lap_value = 0

        self.value_mapping = {
            'Speed Delta': 'speed_value',
            'Lap Delta': 'time_value',
            'Fuel Remaining': 'fuel_value'
        }

        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.set_value)
        self.timer.start(100)

        self.setModal(True)
        self.show()

    def reset(self):
        if self.settings['diff_value'] == 'Last Lap':
            self.compare_lap = self.this_lap

        if self.settings['diff_value'] == 'Best Lap' and \
                len(self.compare_lap) > 0 and len(self.this_lap) > 0 and \
                self.compare_lap[-1].lap_time > self.this_lap[-1].lap_time:
            self.compare_lap = self.this_lap

        self.this_lap = {}

    def update(self, packet):
        dist = math.floor(packet.lap_distance)
        if not dist in self.this_lap:
            self.this_lap[dist] = {'speed': round((packet.speed * 3.6), 1), 'time': round(packet.lap_time, 1)}

        if dist in self.compare_lap:
            speed_diff = round((packet.speed * 3.6) - self.compare_lap[dist]['speed'], 1)
            time_diff = round(self.compare_lap[dist]['time'] - packet.lap_time, 1)

            self.speed_value = speed_diff
            self.time_value = time_diff

        self.fuel_value = packet.fuel_in_tank
        self.current_lap_value = round(packet.lap_time, 3)

    def set_colour(self, label):
        if float(label.text()) < 0:
            label.setPalette(self.red_colour)
        else:
            label.setPalette(self.green_colour)

    def set_value(self):
        self.current_lap.setText(RLCLap.format_time(self.current_lap_value))
        for key, val in self.value_mapping.items():
            if self.settings['center_value'] == key:
                self.center_value.setText(str(getattr(self, val)))
                self.set_colour(self.center_value)

            if self.settings['bottom_left_value'] == key:
                self.bottom_left_value.setText(str(getattr(self, val)))
                self.set_colour(self.bottom_left_value)

            if self.settings['bottom_right_value'] == key:
                self.bottom_right_value.setText(str(getattr(self, val)))
                self.set_colour(self.bottom_right_value)
