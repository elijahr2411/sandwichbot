# Import MySQL connector
import mysql.connector
from mysql.connector import errorcode
# Import the configuration file 
import config
# Connect to the database
# If it fails, throw an error and exit.
try:
	db = mysql.connector.connect(user=config.dbUsername, password=config.dbPassword, host=config.dbAddress, database=config.dbName)
except mysql.connector.Error as err:
	# Access Denied Error
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("\033[1;31mSomething is wrong with your SQL user name or password \033[0;0m")
    raise SystemExit(1)
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
	# db not found error
    print("\033[1;31mDatabase does not exist \033[0;0m")
    raise SystemExit(1)
    # other error
  else:
    print("\033[1;31m" + err + "\033[0;0m")
    raise SystemExit(1)
else:
	# Connected successfully
	print("Successfully connected to database")
