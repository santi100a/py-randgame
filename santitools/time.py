from msilib.schema import SelfReg


class Date:
    from datetime import datetime
    time = datetime.now()
    def get_time(self, base: 12 | 24):
        if base == 12:
            return self.time.strftime("%I:%M:%S %p")
        elif base == 24:
            return self.time.strftime("%H:%M:%S")
        else:
            raise TypeError("Invalid base")
    def get_iso_date(self):
            return self.time.isoformat()
    def refresh(self):
        self.time = self.datetime.now()
        return self