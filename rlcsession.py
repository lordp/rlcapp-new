from rlclap import RLCLap


class RLCSession(object):
    def __init__(self, rlc_web=None):
        self.last_lap = None
        self.current_lap = RLCLap()
        self.fastest_lap = None
        self.top_speed = 0
        self.current_fuel = None
        self.laps = list()

        self.rlc_web = rlc_web
        self.session_number = None

        self.session_type = None
        self.track_length = None
        self.track_number = None

    def new_lap(self):
        print(self.current_lap)
        if self.rlc_web is not None:
            self.rlc_web.send_lap(self.session_number, self.current_lap)

        self.current_lap = RLCLap()
        self.laps.append(self.current_lap)

    def set_lap_values(self, lap_number, lap_time, sector_1, sector_2, sector_3, position, top_speed, current_fuel,
                       drs_used, pits):
        self.current_lap.set_values(lap_number, lap_time, sector_1, sector_2, sector_3, position, top_speed,
                                    current_fuel, drs_used, pits)
        self.new_lap()

    def reset_laps(self):
        self.laps = list()

    def update_values(self, session_type, track_number, track_length):
        self.session_type = session_type
        self.track_length = track_length
        self.track_number = track_number

        if self.rlc_web is not None:
            self.session_number = self.rlc_web.request_session_number(session_type, track_number, track_length)
