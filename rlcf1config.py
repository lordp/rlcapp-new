from PySide import QtGui
import os
from lxml import etree

class RLCF1Config(object):
    def __init__(self, game, path):
        self.game = game.replace('_', ' ')

        self.config_udp = "motion/udp[@enabled='false']"
        self.config_udp_rlc = "motion/udp[@rlc='true']"
        self.config_udp_2016 = None
        self.config_udp_2016_rlc = None

        self.motion = None

        if path == '' or not os.path.exists(path):
            config_path = os.path.expanduser('~\\My Documents\\my games\\{0}\\hardwaresettings').format(self.game)
            self.find_config(config_path)
        else:
            self.config_file = path
            self.motion = self.read_config()

    def find_2016_tag(self, tree):
        for n in range(0, 4):
            tag = "motion/udp{0}[@rlc='true']".format(n)
            if self.config_udp_2016_rlc is None and len(tree.xpath(tag)) > 0:
                self.config_udp_2016_rlc = tag

            tag = "motion/udp{0}[@enabled='false']".format(n)
            if self.config_udp_2016 is None and len(tree.xpath(tag)) > 0:
                self.config_udp_2016 = tag

    def find_config(self, path):
        dialog = QtGui.QFileDialog()
        dialog.setNameFilter("Game Config (hardware_settings_config.xml)")
        dialog.setFileMode(QtGui.QFileDialog.ExistingFile)
        dialog.setDirectory(path)
        if dialog.exec_():
            self.config_file = dialog.selectedFiles()[0]
            self.motion = self.read_config()

    def read_config(self):
        tree = etree.parse(self.config_file)
        self.find_2016_tag(tree)

        motion = None
        try:
            if self.game == 'f1 2015':
                motion = tree.xpath(self.config_udp_rlc)
                if len(motion) == 0:
                    motion = tree.xpath(self.config_udp)
                    if len(motion) == 0:
                        return None
            elif self.game == 'f1 2016':
                if self.config_udp_2016_rlc is not None:
                    motion = tree.xpath(self.config_udp_2016_rlc)
                    if len(motion) == 0:
                        motion = tree.xpath(self.config_udp_2016)
                        if len(motion) == 0:
                            return None
                else:
                    motion = tree.xpath(self.config_udp_2016)
                    if len(motion) == 0:
                        return None

            return motion[0]
        except etree.XMLSyntaxError:
            return motion

    def save_config(self):
        if self.motion.get('rlc') is None:
            self.motion.set('rlc', 'true')

        with open(self.config_file, 'wb') as config:
            config.write(
                etree.tostring(self.motion.getparent().getparent(), encoding='utf-8', xml_declaration=True)
            )

    def enabled(self):
        return self.motion is not None and self.motion.get('enabled') == 'true'

    def toggle_telemetry(self, force_enable=False):
        if self.motion is None:
            return False

        if force_enable:
            self.motion.set('enabled', 'true')
        else:
            self.motion.set('enabled', str(not self.enabled()).lower())

        self.save_config()