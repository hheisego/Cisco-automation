#!/usr/bin/env python
# coding=utf-8
import crassh
import datetime
import time
import sys

# Variables
## devices list:
routers = ["10.232.120.1", "10.233.8.2", "10.232.24.13", "10.232.24.14", "10.232.24.15"]

username = "hheisego"
password = "savehours123"

var1 = len(routers)
var2 = var1

#Date and Time
time = datetime.datetime.now()

filename = raw_input("Introduce the Report file name :  ")  
print filename

#wipe the file to have it clean files :)

open(filename, 'w').close()

# Loop
for device in routers:
	try:
        	f = open(filename, "a+")
		hostname = crassh.connect(device, username, password)
        	output = crassh.send_command("sh int status | in connected ", hostname)
			
        	crassh.disconnect()

# Split the output by spaces so we can search the response -- to be released in v2.0
        	words = output.split()
			
		
		var2 -= 1
		
		print hostname, "Information gathered, writting to file --> ", filename, " remaining: ", var2, "of: ", var1
		

		
#to write output in the report file

		f.write("\r\n\r\n ------>>Hostname: %s<<-----report time: %s-------------------- \r\n\r\n %s " % (hostname, time, output))


	#closing file
		f.close()

	except:
		pass # If connect fails, move onto next router in the list.



