# Cisco devices manual task automation script(s)

Automation script to save life hours by Helmut Heise

-------> Introduction <-------

This document describes how to setup a python script used and intended to automate repetitive / manual work. I have written this document for one colleague who needs to get information from 1000 devices every month for billing purposes, he used to waste at least 5 hours to achieve this, well we simply are wasting now 10 minutes.

-------# Prerequisites / Requirements #--------

Basic Linux knowledge (we are going to focus in Centos this time) / advanced Windows knoledge (process seems more difficult using Windows)

-------| Components Used |-------

- Linux (any flavor), Centos prefered.
- Python 2.7
- Vim editor / nano
- Add the EPEL Repository Pip is part of Extra Packages for Enterprise Linux (EPEL), which is a community repository of non-standard     packages for the RHEL distribution

-------] Configure [-------

  * Install Python and python-pip on Centos (epel for Centos / RHEL must be installed)

        [hheisego@hh-server ~]$ sudo yum -y install python

        [hheisego@hh-server ~]$ sudo yum -y install python-pip

  * Install required libraries
  
  we are going to use crashh library this save me tons of time since functions are really easy to invoke.

    [hheisego@hh-server ~]$ pip install crassh
    
    [hheisego@hh-server ~]$ pip install datetime
    
 ------ } Verify and run { ------
 
  * this is my first github post but i am suspecting that if you clone or download the scripts you may want to give file execution permissions
  
        [hheisego@hh-server ~]$ chmod +x filename.py
    
  **** at least for Linux side, in this first release is a must have performed an ssh to all Cisco devices that script may config or collect information, why? -> the fingerprint key needs to be stored as below example:
  
    [hheisego@hh-server ~]$ ssh heisegoh@10.232.120.1
  
    The authenticity of host '10.232.120.1 (10.232.120.1)' can't be established.
    RSA key fingerprint is SHA256:2NG2v36b1cdRFKbuMqtZez2f2oRAdQjGhqM73cPBpbg.
    Are you sure you want to continue connecting (yes/no)? yes

  **** usage of ts2.py script ****
  
  this script will run the ios command: sh int status | in connected
      
      [hheisego@hh-server ~]$ ./ts2.py
      
        ++ enter the report name
        
  **** usage of acl.py ****
  
  this script will run couple commands in order to delete an acl entry, is an example of how you can adapt these scripts to your environment.
  
      [hheisego@hh-server ~]$ ./acl.py
  
  **** usage of ts3.py script ****
  
  Basically what we need here is to place a text file with the name ipaddr.txt in the same folder where the script is located, this  text file must have the ip addresses (one address per line), it runs like ts2.py but using the ip addresses listed in the text file.
  
  if something goes wrong please contact me at hheisego@gmail.com
   
