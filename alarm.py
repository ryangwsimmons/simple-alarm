from datetime import time

class Alarm:

    def __init__(self, time = None):
        self._time = time
    
    @property
    def time(self):
        return self._time
    
    @time.setter
    def time(self, time):
        self._time = time

    @property
    def hour(self):
        return self._time.hour
    
    @hour.setter
    def hour(self, hour):
        self._time.hour = hour
    
    @property
    def minute(self):
        return self._time.minute
    
    @minute.setter
    def minute(self, minute):
        self._time.minute = minute