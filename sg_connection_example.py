import pprint # Useful for debugging

import shotgun_api3

SERVER_PATH = "https://your_site.shotgunstudio.com"
SCRIPT_NAME = 'my_script'
SCRIPT_KEY = '27b65d7063f46b82e670fe807bd2b6f3fd1676c1'

sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)

# Just for demo purposes, this will print out property and method names available on the
# sg connection object
pprint.pprint([symbol for symbol in sorted(dir(sg)) if not symbol.startswith('_')])