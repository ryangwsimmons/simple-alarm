from alarm import Alarm
from datetime import datetime, time
import sys
from time import time, sleep
import typing

class AlarmClock:

    def __init__(self, alarm = None):
        # If an alarm has been set in the constructor, set the alarm attribute (otherwise, set it to None)
        if alarm == None:
            self._alarm = Alarm()
        else:
            self._alarm = alarm
    
    @property
    def alarm(self):
        return self._alarm
    
    @alarm.setter
    def alarm(self, alarm):
        # Set an alarm on the alarm clock
        self._alarm = alarm
    
    def check_time(self):
        if datetime.now() < self._alarm._time:
            return False
        else:
            return True
    
    def monitor(self):
        # Wait until the alarm time is the current time
        while self.check_time() == False:
            pass
        else:
            return
    
    @property
    def ringing(self):
        return self._ringing
    
    @ringing.setter
    def ringing(self, flag):
        self._ringing = flag
    
    def ring(self):
        # Turn on the alarm ring
        self._ringing = True

        # While the attribute is true, play the alarm
        while self._ringing == True:
            sys.stdout.write("\a")
            sleep(0.5)
            sys.stdout.write("\a")
            sleep(0.5)
            sys.stdout.write("\a")

            sleep(2)