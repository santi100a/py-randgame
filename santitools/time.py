class Date:
    import datetime
    time = datetime.datetime.now()
    def getTime(self, base: 12 | 24):
        if base == 12:
            return self.time.strftime("%I:%M:%S %p")
        elif base == 24:
            return self.time.strftime("%H:%M:%S")
        else:
            raise TypeError("Invalid base")

            
