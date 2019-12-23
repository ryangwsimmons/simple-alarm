from alarm import Alarm
from datetime import datetime, time
import sys
from time import time

class AlarmClock:

    def __init__(self, alarm = None):
        # If an alarm has been set in the constructor, set the alarm attribute (otherwise, set it to None)
        self.alarm = alarm
    
    def set_alarm(self, alarm):
        # Set an alarm on the alarm clock
        self.alarm = alarm
    
    def monitor(self):
        # Wait until the alarm time is the current time
        while datetime.now().time != self.alarm.time:
            pass
        else:
            return
    
    @property
    def ringing(self):
        return self.ringing
    
    @ringing.setter
    def ringing(self, flag):
        self.ringing = flag
    
    def ring(self):
        # Turn on the alarm ring
        self.ringing = True

        # While the attribute is true, play the alarm
        while self.ringing == True:
            sys.stdout.write("\a")
            time.sleep(0.5)
            sys.stdout.write("\a")
            time.sleep(0.5)
            sys.stdout.write("\a")

            time.sleep(2)