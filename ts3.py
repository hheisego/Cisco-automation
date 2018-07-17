#!/usr/bin/env python
# coding=utf-8
import crassh
import datetime
import time
import sys
from termcolor import colored, cprint

# Variables


username = "hheisego"
password = "savetime123"



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





#ciclo de escritora 

                f.write("\r\n\r\n ------>>Hostname: %s<<-----report time: %s-------------------- \r\n\r\n %s " % (hostname, time, output))


        #closing ffile
                f.close()



        except:
                pass # If connect fails, move onto next router in the list.
