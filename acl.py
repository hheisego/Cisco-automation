#!/usr/bin/env python
# coding=utf-8
import crassh
import datetime
import time
import sys


# Variables
routers = ["10.236.58.66", "10.237.179.66", "10.237.180.66 "]
username = "heisegoh"
password = "Welcome123"
# Loop
for device in routers:
        try:
                hostname = crassh.connect(device, username, password)
                output = crassh.send_command("conf t", hostname)
                output1 = crassh.send_command("ip access-list standard 89", hostname)
                output2 = crassh.send_command("no 10", hostname)
                output3 = crassh.send_command("no 20", hostname)
                output4 = crassh.send_command("exit", hostname)
                output5 = crassh.send_command("no snmp-server host 10.193.135.12 version 2c Wr7j4p3vi9pe9eth", hostname)
                output6 = crassh.send_command("no snmp-server host 10.193.135.13 version 2c Wr7j4p3vi9pe9eth", hostname)
                # commented or disabled output7 = crassh.send_command("do show run | in snmp", hostname)
                #output8 = crassh.send_command("do write", hostname)
                #output9 = crassh.send_command("write", hostname)
                
                #output5 * crassh.send_command("write", hostname)
                crassh.disconnect()
# Split the output by spaces so we can search the response
                words = output7.split()
                
                # Look for "public" in the output
                #for x in words:
                #        if x == "snmp-server host 10.193.135.12 version 2c Wr7j4p3vi9pe9eth":
                #                print "flag"
                #        else:
                #                print "SNMP parameter removed."

		print "Commands performed \r\n", output, "\r\n ", output1, "\r\n", output2, "\r\n", output3, "\r\n", output4, "\r\n", output5, "\r\n", output6, "\r\n", output8
                #print output8, "\r\n", output9
                                                                                
		#print "Configuration performed in host: ",hostname, "\r\n", output1, "\r\n", output2, "\r\n", output3, "\r\n", output5 


        except:
                pass # If connect fails, move onto next router in the list.
        
        
