from alarm import Alarm
from alarmclock import AlarmClock
from datetime import datetime, time, timedelta
import gui
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk
from threading import Thread
from time import sleep

class AlarmController:

    def __init__(self, gui):
        # Set the controller's GUI to the given GUI
        self.gui = gui

        # Create the controller's alarm clock
        self.clock = AlarmClock()
    
    def set_alarm(self, button):
        # Disable the hour and minute setters, the set button
        self.gui.hours_setter.set_sensitive(False)
        self.gui.minutes_setter.set_sensitive(False)
        self.gui.set_button.set_sensitive(False)

        # Get the hour and minutes from the GUI
        hours = self.gui.hours_setter.get_value_as_int()
        minutes = self.gui.minutes_setter.get_value_as_int()

        # Create a new time object with the hour and minute values
        # If the alarm time is less than the current time, set the alarm for tomorrow, else set it for today
        if hours < datetime.now().hour or (minutes <= datetime.now().minute and hours <= datetime.now().hour):
            self.clock._alarm._time = datetime.now().replace(day=(datetime.now().day + 1), hour=hours, minute=minutes, second=0, microsecond=0)
        else:
            self.clock._alarm._time = datetime.now().replace(hour=hours, minute=minutes, second=0, microsecond=0)

        # Start the monitor for the alarm, then open the alarm dialog
        monitor_thread = Thread(target=self.start_alarm)
        monitor_thread.daemon = True
        monitor_thread.start()
    
    def set_time_remaining(self):
        #Calculate the difference between the current time and the alarm time
        time_difference = self.clock._alarm._time - datetime.now()

        # While the alarm has yet to ring, count down the time remaining on the status bar
        while self.clock.ringing != True:
            # Calculate the hours, minutes, and seconds remaining
            hours = int((time_difference.seconds / (60 ** 2)))
            minutes = int((time_difference.seconds / 60) - (hours * 60))
            seconds = int((time_difference.seconds) - (hours * (60 ** 2)) - (minutes * 60))

            # Push the time remaining to the status bar, after removing any previous messages
            self.gui.time_remaining_bar.remove_all(0)
            self.gui.time_remaining_bar.push(0, "Time Until Alarm: " + str(hours) + (" hour, " if hours < 2 and hours > 0 else " hours, ") \
                                                                + str(minutes) + (" minute, " if minutes < 2 and minutes > 0 else " minutes, ") \
                                                                + str(seconds) + (" second" if seconds < 2 and seconds > 0 else " seconds"))
            
            # Calculate the new time remaining
            time_difference = timedelta(seconds=(time_difference.seconds - 1))

            # Wait a second before doing it again
            sleep(1)
        self.gui.time_remaining_bar.remove_all(0)

    def start_alarm(self):
        # Create a new thread to display the time remaining until the alarm
        time_remaining_thread = Thread(target=self.set_time_remaining)
        time_remaining_thread.daemon = True
        time_remaining_thread.start()

        #Wait for the time to reach the alarm time
        self.clock.wait_for_time()

        ringing_thread = Thread(target=self.clock.ring)
        ringing_thread.daemon = True
        ringing_thread.start()
        GLib.idle_add(self.open_ring_dialog)
    
    def open_ring_dialog(self):
        # Open the ringing dialog
        ringing_dialog = Gtk.MessageDialog(self.gui, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Alarm is ringing! Press OK to dismiss.")
        ringing_dialog.run()
        ringing_dialog.destroy()

        # Stop the ringing
        self.clock.ringing = False

        # Re-enable UI elements
        self.gui.hours_setter.set_sensitive(True)
        self.gui.minutes_setter.set_sensitive(True)
        self.gui.set_button.set_sensitive(True)