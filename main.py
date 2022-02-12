# Import some stuff
from pathlib import Path
import nextcord
import nextcord.ext
from time import sleep
# Startup ascii
print("\033[132m")
print("====================")
print("=== Sandwich Bot ===")
print("==== Early Beta ====")
print("====================")
print("Not nearly ready for production.")
print("Most features have not been implemented.")
print("(c) 2022 Elijah R")
print("This software is released under the GNU General Public License, Version 3 under absolutely NO WARRANTY, to the extent allowed by applicable law")
print("\033[00m")
sleep(1)
#  Make sure the user has created the config file.
if Path("config.py").is_file():
	print("Configuration file found")
	#import the config file
	from config import cfg
else:
	#throw an error and exit
	print("\033[131mConfiguration file not found.")
	print("Did you forget to rename and edit the example file? \033[00m")
	raise SystemExit(1)
# Import command and SQL modules
from botmods.botcommands import *
from botmods.sql import *
# Connect to discord and start the bot.
# If it fails, throw an error and exit
print("Starting bot...")
try:
	bot.run(cfg("botToken"))
except:
	print("\033[131mFailed to login to Discord as bot. \033[00m")
