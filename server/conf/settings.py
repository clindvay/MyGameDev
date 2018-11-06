"""
Evennia settings file.

The available options are found in the default settings file found
here:

/home/pi/muddev/evennia/evennia/settings_default.py

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

If you want to share your game dir, including its settings, you can
put secret game- or server-specific settings in secret_settings.py.

"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "mygame"


######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")

#Added for Email Login requirement contrib.
#CMDSET_UNLOGGEDIN = "contrib.email_login.UnloggedinCmdSet"

#Added for LOGIN MENU rather than connect/create command logins.
#CMDSET_UNLOGGEDIN = "contrib.menu_login.UnloggedinCmdSet"

MULTISESSION_MODE=1
COMMAND_RATE_WARNING = "Slow down! SLOW DOWN! Now what were you saying?"
MAX_CHAR_LIMIT_WARNING = "Will you stop rambling on and get to the point!" 
