#!/usr/bin/env python
# coding=utf-8
import crassh
import datetime
import time
#import sleep
import sys

# Variables
##routers = ["10.232.120.1", "10.233.8.2", "10.232.24.13", "10.232.24.14", "10.232.24.15"]

routers = ["10.232.120.1", "10.233.8.2", "10.232.24.13", "10.232.24.14", "10.232.24.15", "10.232.248.2", "10.232.248.3", "10.232.248.11",
		   "10.232.248.12", "10.232.248.13", "10.232.248.14", "10.232.248.15", "10.232.248.16", "10.232.248.17", "10.232.248.18", "10.232.248.19"] 

username = "heisegoh"
password = "Welcome123"

var1 = len(routers)
var2 = var1
#Date and Time

time = datetime.datetime.now()

filename = raw_input("Introduce the Report file name :  ")  # Python 2
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

# Split the output by spaces so we can search the response
        	words = output.split()
			
		
		var2 -= 1
		
		print hostname, "Information gathered, writting to file --> ", filename, " remaining: ", var2, "of: ", var1
		
# progress bar
		#progress = progressbar.ProgressBar()
		#for i in progress(range(80)):
		#	time.sleep(0.01)
		
		
		
#ciclo de escritora del pinche archivo
#	for i in range(2):
		f.write("\r\n\r\n ------>>Hostname: %s<<-----report time: %s-------------------- \r\n\r\n %s " % (hostname, time, output))


	#closing fucking fil
		f.close()

	except:
		pass # If connect fails, move onto next router in the list.


