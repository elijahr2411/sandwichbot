import mysql.connector
from mysql.connector import errorcode
import config
try:
	db = mysql.connector.connect(user=config.dbUsername, password=config.dbPassword, host=config.dbAddress, database=config.dbName)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("\033[1;31mSomething is wrong with your SQL user name or password \033[0;0m")
    raise SystemExit(1)
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("\033[1;31mDatabase does not exist \033[0;0m")
    raise SystemExit(1)
  else:
    print("\033[1;31m" + err + "\033[0;0m")
    raise SystemExit(1)
else:
	print("Successfully connected to database")
