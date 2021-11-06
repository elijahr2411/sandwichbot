from time import sleep
print("\033[1;32m")
print("====================")
print("=== Sandwich Bot ===")
print("==== Early Beta ====")
print("====================")
print("Not nearly ready for production.")
print("Most features have not been implemented.")
print("\033[0;0m");
sleep(1);

from pathlib import Path
if Path("config.py").is_file():
	print("Configuration file found")
	import config
else:
	print("\033[1;31mConfiguration file not found.")
	print("Did you forget to rename and edit the example file? \033[0;0m")
	raise SystemExit(1)

import nextcord
import nextcord.ext
from botmods.botcommands import *
from botmods.sql import *

try:
	bot.run(config.botToken)
except:
	print("\033[1;31mFailed to login to Discord as bot. \033[0;0m")
else:
	print("Successfully logged into Discord as bot.")
