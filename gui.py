import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class AlarmGui(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Alarm", default_width=200, default_height=100, resizable=False)

        # Define the main box for the application
        self.main_box = Gtk.Box(border_width=5, spacing=2, orientation=Gtk.Orientation.VERTICAL)

        # Define the horizontal box for the selectors and labels to be placed in
        self.selectors_box = Gtk.Box(spacing=1, orientation=Gtk.Orientation.HORIZONTAL)

        # Define the vertical box for widgets related to hours to be placed in
        self.hours_box = Gtk.Box(spacing=1, orientation=Gtk.Orientation.VERTICAL)

        # Define the separator for hours and minutes
        self.separator = Gtk.Label(valign=Gtk.Align.CENTER, margin_bottom=15)
        self.separator.set_markup('<span size="xx-large">:</span>')

        # Define the vertical box for widgets related to minutes to be placed in
        self.minutes_box = Gtk.Box(spacing=1, orientation=Gtk.Orientation.VERTICAL)

        # Define the SpinButton to set hours
        self.hours_setter = Gtk.SpinButton(value=0, orientation=Gtk.Orientation.VERTICAL, 
            adjustment=Gtk.Adjustment(value=0, lower=0, upper=24, step_increment=1))
        self.hours_setter.set_range(0, 23)

        # Define the label for the hours setter
        self.hours_label = Gtk.Label(label="Hour")

        # Define the SpinButton to set minutes
        self.minutes_setter = Gtk.SpinButton(value=0, orientation=Gtk.Orientation.VERTICAL, 
            adjustment=Gtk.Adjustment(value=0, lower=0, upper=60, step_increment=1))
        self.minutes_setter.set_range(0, 59)
        def output_two_digits(spinbutton):
            spinbutton.props.text = "%02d" % spinbutton.props.value
            return True
        self.minutes_setter.connect('output', output_two_digits)

        # Define the label for the minutes setter
        self.minutes_label = Gtk.Label(label="Minute")

        # Define the button to set the alarm
        self.set_button = Gtk.Button(label="Set Alarm")

        # Define the status bar to display the time until the alarm goes off
        self.time_remaining_bar = Gtk.Statusbar.new()

        # Arrange widgets correctly in the window
        self.add(self.main_box)
        self.main_box.pack_start(self.selectors_box, True, True, 0)

        self.selectors_box.pack_start(self.hours_box, True, True, 0)
        self.selectors_box.pack_start(self.separator, True, True, 0)
        self.selectors_box.pack_start(self.minutes_box, True, True, 0)

        self.hours_box.pack_start(self.hours_setter, True, True, 0)
        self.hours_box.pack_start(self.hours_label, True, True, 0)

        self.minutes_box.pack_start(self.minutes_setter, True, True, 0)
        self.minutes_box.pack_start(self.minutes_label, True, True, 0)

        self.main_box.pack_start(self.set_button, True, False, 0)
        self.main_box.pack_start(self.time_remaining_bar, True, True, 0)