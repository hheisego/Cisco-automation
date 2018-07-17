#!/usr/bin/env python
# coding=utf-8
import crassh
import datetime
import time
import sys
from termcolor import colored, cprint

# Variables

routers = ["10.232.120.1", "10.233.8.2", "10.232.24.13", "10.232.24.14", "10.232.24.15", "10.232.248.2", "10.232.248.3", "10.232.248.11",
                   "10.232.248.12", "10.232.248.13", "10.232.248.14", "10.232.248.15", "10.232.248.16", "10.232.248.17", "10.232.248.18", "10.232.248.19"] 

username = "heisegoh"
password = "Welcome123"


# var1 = len(routers) before reading damn ipaddr.txt file


# var2 = var1 old script

#read ip addresses from text file line by line

filename = "ipaddr.txt"

f = open(filename, "a+")
 
routers2 = f.read().split("\n")

#to remove the last line in the text file..
del routers2[-1]

#print lines, "\r\n"

var1 = len(routers2)
var2 = var1
#print tam

f.close() # Close file


#Date and Time

time = datetime.datetime.now()

filename = raw_input("Introduce the Report file name :  ")  # Python 2
print filename

#wipe the file to have it clean files :)

open(filename, 'w').close()

# Loop
for device in routers2:
        try:
                f = open(filename, "a+")
                hostname = crassh.connect(device, username, password)
                output = crassh.send_command("sh int status | in connected ", hostname)

                crassh.disconnect()

# Split the output by spaces so we can search the response
                words = output.split()


                var2 -= 1

                print "Information collected for: ",hostname ,"| Writting to file->", filename, "| Remaining:", var2, "of:", var1

                if var2 == 0:
                        cprint('\n\n ---------------- Success !!! --------------', 'green', attrs=['blink'])


# progress bar
                #progress = progressbar.ProgressBar()
                #for i in progress(range(80)):
                #       time.sleep(0.01)



#ciclo de escritora del pinche archivo
#       for i in range(2):
                f.write("\r\n\r\n ------>>Hostname: %s<<-----report time: %s-------------------- \r\n\r\n %s " % (hostname, time, output))


        #closing fucking fil
                f.close()



        except:
                pass # If connect fails, move onto next router in the list.
