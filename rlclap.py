from decimal import Decimal


class RLCLap(object):
    def __init__(self):
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

    def set_values(self, lap_number, lap_time, sector_1, sector_2, sector_3, position, top_speed,
                   current_fuel, drs_used, pits):
        self.lap_number = lap_number
        self.lap_time = round(Decimal(lap_time), 3)
        self.sector_1 = round(Decimal(sector_1), 3)
        self.sector_2 = round(Decimal(sector_2), 3)
        self.sector_3 = round(Decimal(sector_3), 3)
        self.position = position
        self.top_speed = round(Decimal(top_speed), 3)
        self.current_fuel = round(Decimal(current_fuel), 3)
        self.drs_used = drs_used
        self.pits = pits

    @staticmethod
    def format_time(seconds):
        m, s = divmod(seconds, 60)
        if m > 0:
            return '{0:.0f}:{1:06.3f}'.format(m, s)
        else:
            return '{0:06.3f}'.format(s)

    def format_times(self):
        fs1 = self.format_time(self.sector_1)
        fs2 = self.format_time(self.sector_2)
        fs3 = self.format_time(self.sector_3)
        flt = self.format_time(self.lap_time)

        return {"sector_1": fs1, "sector_2": fs2, "sector_3": fs3, "lap_time": flt}

    def __str__(self):
        return "Lap {0}: {1} {2} {3} {4} {5} {6} {7} {8} {9}".format(
            int(self.lap_number), self.lap_time, self.sector_1, self.sector_2, self.sector_3,
            self.position, self.top_speed, self.current_fuel, self.drs_used, self.pits
        )
