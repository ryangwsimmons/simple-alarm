import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

from gui import AlarmGui

gui = AlarmGui()
gui.connect("destroy", Gtk.main_quit)
gui.show_all()
Gtk.main()