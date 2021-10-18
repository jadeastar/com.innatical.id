import gi
import webview
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    #show the page
webview.create_window('Innatical ID', 'https://id.innatical.com')
webview.start()

#kill the app when x is pressed
def on_window1_destroy(self, *args):    
    webview.end()
    exit()
    #The program won't exit for some fucking bullshit reason. Killing the webview is ok for now. This will cause some fucking scandal later.

# Create a new application
app = Gtk.Application(application_id='com.innatical.id')
app.connect('activate', on_activate)

# Run the application
app.run(None)
