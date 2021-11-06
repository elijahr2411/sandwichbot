# Import some stuff
from pathlib import Path
import nextcord
import nextcord.ext
from time import sleep
# Startup ascii
print("\033[1;32m")
print("====================")
print("=== Sandwich Bot ===")
print("==== Early Beta ====")
print("====================")
print("Not nearly ready for production.")
print("Most features have not been implemented.")
print("\033[0;0m");
sleep(1);
#  Make sure the user has created the config file.
if Path("config.py").is_file():
	print("Configuration file found")
	#import the config file
	import config
else:
	#throw an error and exit
	print("\033[1;31mConfiguration file not found.")
	print("Did you forget to rename and edit the example file? \033[0;0m")
	raise SystemExit(1)
# Import command and SQL modules
from botmods.botcommands import *
from botmods.sql import *
# Connect to discord and start the bot.
# If it fails, throw an error and exit
try:
	bot.run(config.botToken)
except:
	print("\033[1;31mFailed to login to Discord as bot. \033[0;0m")
else:
	print("Successfully logged into Discord as bot.")
