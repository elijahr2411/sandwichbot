import nextcord
import nextcord.ext
# import mysqlclient.connector
from pathlib import Path
from botmods.botcommands import *
if Path("config.py").is_file():
	print("Configuration file found")
	import config
else:
	print("\033[1;31mConfiguration file not found.")
	print("Did you forget to rename and edit the example file? \033[0;0m")
	raise SystemExit(1)
bot.run(config.botToken)
