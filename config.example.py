#####################
# BOT CONFIGURATION #
#####################

# Before use of this bot, please rename this file to config.py and fill out all fields.
# Not doing this will result in a fatal error.

# Bot Token
botToken = ""

# Database address
dbAddress = "127.0.0.1"

# Database name
dbName = "sandwichbot"

# Database username
dbUsername = "username"

# Database password
dbPassword = "password"
######################
# STOP EDITING HERE  #
######################
def cfg(cfgval):
	if cfgval == "botToken":
		return(botToken)
	if cfgval == "dbAddress":
		return(dbAddress)
	if cfgval == "dbName":
		return(dbName)
	if cfgval == "dbUsername":
		return(dbUsername)
	if cfgval == "dbPassword":
		return(dbPassword)
