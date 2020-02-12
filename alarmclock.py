from alarm import Alarm
from datetime import datetime, time
from playsound import playsound
from time import sleep

class AlarmClock:

    def __init__(self, alarm = None):
        # If an alarm has been set in the constructor, set the alarm attribute (otherwise, set it to None)
        if alarm == None:
            self._alarm = Alarm()
        else:
            self._alarm = alarm
        
        self._ringing = False
    
    @property
    def alarm(self):
        return self._alarm
    
    @alarm.setter
    def alarm(self, alarm):
        # Set an alarm on the alarm clock
        self._alarm = alarm
    
    def wait_for_time(self):
        #Calculate the difference between the current time and the alarm time
        time_difference = self._alarm._time - datetime.now()

        #Sleep for the difference between the two times
        sleep(time_difference.total_seconds())
    
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
            playsound("alarm.wav")
            sleep(2)