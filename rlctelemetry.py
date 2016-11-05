from PySide import QtGui
import rlctelemetryui


class RLCTelemetry(QtGui.QDialog, rlctelemetryui.Ui_Dialog):
    def __init__(self, parent=None):
        super(RLCTelemetry, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle('Telemetry')

        self.red_colour = QtGui.QPalette()
        self.red_colour.setColor(QtGui.QPalette.WindowText, QtGui.QColor('#FF0000'))

        self.green_colour = QtGui.QPalette()
        self.green_colour.setColor(QtGui.QPalette.WindowText, QtGui.QColor('#00FF00'))

        self.black_colour = QtGui.QPalette()
        self.black_colour.setColor(QtGui.QPalette.Window, QtGui.QColor('#000000'))
        self.setPalette(self.black_colour)

        self.setModal(True)
        self.show()
