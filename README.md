# Cisco-automation
Automation script to save life hours by Helmut Heise

-------> Introduction <-------

This documents describes how to setup a python script used and intended automate repetitive manual work. I have written this document for one colleague who needs to get information from 1000 devices every month for billing purposes, he used to waste at least 5 hours to achieve this, well we simply are wasting now 10 minutes.

-------# Prerequisites / Requirements #--------

Basic Linux knowledge (we are going to focus in Centos this time) / advanced Windows knoledge (process seems more difficult using Windows)

-------| Components Used |-------

- Linux (any flavor), Centos prefered.
- Python 2.7
- Vim editor / nano

-------] Configure [-------

  * Install Python and python-pip on Centos

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
  
  [hheisego@hh-vorwerk ~]$ ssh heisegoh@10.232.120.1
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
  
  
     
