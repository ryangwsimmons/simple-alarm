from datetime import time

class Alarm:

    def __init__(self, time):
        self.time = time
    
    @property
    def time(self):
        return self.time
    
    @time.setter
    def time(self, time):
        self.time = time

    @property
    def hour(self):
        return self.time.hour
    
    @hour.setter
    def hour(self, hour):
        self.time.hour = hour
    
    @property
    def minute(self):
        return self.time.minute
    
    @minute.setter
    def minute(self, minute):
        self.time.minute = minute