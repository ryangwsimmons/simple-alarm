from alarm import Alarm
from alarmclock import AlarmClock
from datetime import datetime, time
import gui
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from threading import Thread

class AlarmController:

    def __init__(self, gui):
        # Set the controller's GUI to the given GUI
        self.gui = gui

        # Create the controller's alarm clock
        self.clock = AlarmClock()
    
    def set_alarm(self, button):
        # Get the hour and minutes from the GUI
        hours = self.gui.hours_setter.get_value_as_int()
        minutes = self.gui.minutes_setter.get_value_as_int()

        # Create a new time object with the hour and minute values
        self.clock._alarm._time = datetime.now().replace(hour=hours, minute=minutes)

        # Start the monitor for the alarm, then open the alarm dialog
        monitor_thread = Thread(target=self.start_alarm)
        monitor_thread.daemon = True
        monitor_thread.start()

    def start_alarm(self):
        self.clock.monitor()
        ringing_thread = Thread(target=self.clock.ring)
        ringing_thread.daemon = True
        ringing_thread.start()
        self.open_ring_dialog()
    
    def open_ring_dialog(self):
        ringing_dialog = Gtk.MessageDialog(self.gui, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Alarm is ringing! Press OK to dismiss.")
        ringing_dialog.run()
        self.clock.ringing = False