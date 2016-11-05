import requests
from decimal import Decimal


class RLCWeb(object):
    def __init__(self, parent, driver, race, token):
        self.session_url = 'https://racingleaguecharts.com/sessions/register.json'
        self.lap_url = 'https://racingleaguecharts.com/laps.json'

        self.driver = driver
        self.race = race
        self.token = token

        self.parent = parent

        self.session_number = 0
        self.session_link = None

    def request_session_number(self, session_type, track_number, track_length):
        track_length = round(Decimal(track_length), 3)
        payload = {
            "track": track_number,
            "track_size": track_length,
            "type": session_type,
            "driver": self.driver,
            "race": self.race,
            "token": self.token
        }

        self.session_number = self.send_request(self.session_url, payload)
        self.session_link = 'https://racingleaguecharts.com/sessions/{0}'.format(self.session_number)

        self.parent.session_link.setText(self.session_link)

        return self.session_number

    def send_lap(self, session_number, lap):
        formatted_times = lap.format_times
        payload = {
            "session_id": session_number, "lap_number": lap.lap_number, "position": lap.position,
            "sector_1": lap.sector_1, "sector_2": lap.sector_2, "sector_3": lap.sector_3,
            "total": lap.lap_time, "formatted_total": formatted_times['total'], "speed": lap.top_speed,
            "fuel": lap.current_fuel, "drs_used": lap.drs_used, "pitted": lap.pitted
        }

        return self.send_request(self.lap_url, payload)

    def send_request(self, url, payload, attempts=0):
        if attempts > 4:
            return False

        r = requests.post(url, data=payload)
        if r.status_code == 200:
            if url == self.session_url:
                return r.json()['session_id']
        else:
            attempts += 1
            self.send_request(url, payload, attempts)
