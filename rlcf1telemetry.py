from f1_definitions import SF1
from rlcsession import RLCSession
from socket import *
import threading
import ctypes


class RLCF1Telemetry(threading.Thread):
    def __init__(self, parent, rlc_web=None, telemetry_settings=None):
        threading.Thread.__init__(self)

        self.parent = parent

        self.packets = list()
        self.rlc_web = rlc_web
        self.session = RLCSession(self.rlc_web)

        self.telemetry_window = None
        if telemetry_settings['enabled'] == 'True':
            from rlctelemetry import RLCTelemetry
            self.telemetry_window = RLCTelemetry(telemetry_settings)

        self.session_type = None
        self.track_number = None
        self.track_length = None

        self.lap_time = None
        self.lap_number = None
        self.sector_1 = None
        self.sector_2 = None
        self.sector_3 = None
        self.position = None
        self.top_speed = None
        self.current_fuel = None
        self.drs_used = None
        self.pits = None

        self.set_lap_defaults()

        self.running = True

        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.socket.bind(('', 20777))

        self.receive_size = ctypes.sizeof(SF1)
        self.buffer = bytearray(self.receive_size)

        self.parent.show_message('F1 telemetry system started')

        self.daemon = True
        self.start()

    def set_lap_defaults(self):
        self.lap_time = 0
        self.lap_number = 0
        self.sector_1 = 0
        self.sector_2 = 0
        self.sector_3 = 0
        self.position = 0
        self.top_speed = 0
        self.current_fuel = 0
        self.drs_used = 0
        self.pits = 0

    def set_session_values(self, session_type=None, track_number=None, track_length=None):
        update_session = False
        if session_type is not None and session_type != self.session_type:
            self.session_type = session_type
            update_session = True

        if track_length is not None and track_length != self.track_length:
            self.track_length = track_length
            update_session = True

        if track_number is not None and track_number != self.track_number:
            self.track_number = track_number
            update_session = True

        if update_session:
            self.session.update_values(session_type, track_number, track_length)

    def set_lap_values(self, sector_1_time=0, sector_2_time=0, top_speed=0, fuel=0, position=0,
                       drs_used=0, pits=0):
        if sector_1_time > 0 and self.sector_1 == 0:
            self.sector_1 = sector_1_time

        if sector_2_time > 0 and self.sector_2 == 0:
            self.sector_2 = sector_2_time

        if top_speed > 0 and self.top_speed < top_speed:
            self.top_speed = top_speed

        if fuel > 0:
            self.current_fuel = fuel

        if position > 0:
            self.position = position

        if drs_used > 0:
            self.drs_used = drs_used

        if pits > 0:
            self.pits = pits

    def finalise_lap(self, lap_time, lap_number):
        self.lap_time = lap_time
        self.lap_number = lap_number
        self.sector_3 = self.lap_time - (self.sector_1 + self.sector_2)

        self.session.set_lap_values(self.lap_number, self.lap_time, self.sector_1, self.sector_2, self.sector_3,
                                    self.position, self.top_speed, self.current_fuel, self.drs_used, self.pits)

        if self.telemetry_window is not None:
            self.telemetry_window.reset()

    def check_new_session(self, session_type=None, track_number=None, track_length=None):
        if session_type is not None and session_type != self.session_type or \
                track_number is not None and track_number != self.track_number:
            self.session = RLCSession(self.rlc_web)
            self.set_session_values(session_type, track_number, track_length)

    def close(self):
        self.parent.show_message('F1 telemetry system stopped')
        self.running = False

    def run(self):
        while self.running:
            self.socket.recv_into(self.buffer)
            packet = SF1.from_buffer(self.buffer)

            self.set_session_values(packet.session_type, packet.track_number, packet.track_length)
            self.check_new_session(packet.session_type, packet.track_number)

            self.set_lap_values(packet.sector_1_time, packet.sector_2_time, packet.speed,
                                packet.fuel_in_tank, packet.car_position, packet.drs,
                                packet.in_pits)

            if packet.lap_time == 0:
                self.finalise_lap(packet.last_lap_time, packet.lap - 1)
                self.set_lap_defaults()
                del self.packets[:]

            self.packets.append(packet)

        self.socket.close()
