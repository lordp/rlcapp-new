import requests
from decimal import Decimal


class RLCWeb(object):
    def __init__(self, parent, driver, race, token):
        self.driver = driver
        self.race = race
        self.token = token

        self.parent = parent

        self.session_number = 0
        self.session_link = None

        domain = 'https://racingleaguecharts.com'

        self.urls = {
            'session': {
                'url': "{0}/sessions/register.json".format(domain),
                'method': 'post',
                'return': 'session_id'
            },
            'lap': {
                'url': "{0}/laps.json".format(domain),
                'method': 'post',
                'return': 'lap_id'
            },
            'driver': {
                'url': "{0}/drivers.json?token={1}".format(domain, self.token),
                'method': 'get',
                'return': 'drivers'
            },
            'races': {
                'url': "{0}/races/app.json".format(domain),
                'method': 'get',
                'return': 'races'
            }
        }

    def request_drivers(self):
        return self.send_request(self.urls['driver'], None)

    def request_session_number(self, session_type, track_number, track_length):
        self.session_number = 0
        track_length = round(Decimal(track_length), 3)
        payload = {
            "track": int(track_number),
            "track_size": track_length,
            "type": int(session_type),
            "driver": self.driver,
            "race": self.race,
            "token": self.token
        }

        self.session_number = self.send_request(self.urls['session'], payload)
        self.session_link = '<a href="https://racingleaguecharts.com/sessions/{0}">' \
                            'https://racingleaguecharts.com/sessions/{0}' \
                            '</a>'.format(self.session_number, self.session_number)

        return self.session_number

    def send_lap(self, session_number, lap):
        formatted_times = lap.format_times()
        payload = {
            "session_id": session_number, "lap_number": lap.lap_number, "position": lap.position,
            "sector_1": lap.sector_1, "sector_2": lap.sector_2, "sector_3": lap.sector_3,
            "total": lap.lap_time, "formatted_total": formatted_times['lap_time'], "speed": lap.top_speed,
            "fuel": lap.current_fuel, "drs_used": lap.drs_used, "pitted": lap.pits
        }

        return self.send_request(self.urls['lap'], payload)

    def send_request(self, url, payload, attempts=0):
        if attempts > 4:
            return False

        r = getattr(requests, url['method'])(url['url'], data=payload)
        if r.status_code == 200:
            return r.json()[url['return']]
        else:
            attempts += 1
            self.send_request(url, payload, attempts)
