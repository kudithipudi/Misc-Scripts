#!/usr/bin/env python
#
#authServerFW.py: Script to update IPTables for allowing access publishing
#               from Authoring server
__author__      = "Vinay Kudithipudi"

#Importing modules
import os
import sys
import glob
from optparse import OptionParser

def firewallFlush():
        os.system('sudo iptables --flush')
        return


def firewallRuleChange(host):
        serverName = host
        firewallCommand = "sudo iptables -A OUTPUT -d "+serverName+" -j DROP"
        os.system(firewallCommand)
        return

def saveFirewallState():
        systemCommand = "sudo service iptables save"
        os.system(systemCommand)
        return

def logToSyslog(logPreFix, message):
        messageToLog = logPreFix + message
        messageToLog = "logger " + messageToLog
        os.system(messageToLog)
        return

def generateServerNames(environmentID):
        tempEnvironment = environmentID
        serverList=[]
        for i in [1, 2, 3, 4, 5, 6]:
                serverName = "pil-vm-app-"+str(tempEnvironment)+str(i)+".aircell.prod"
                serverList.append(serverName)
        return serverList

# Option Parsing Tool --help for help
parser = OptionParser(description="Script to modify the host firewall to allow publishinng", epilog="Report bugs to: Vinay Kudithipudi <vkudithipudi@gogoair.com>", version="%prog v1.0")
parser.add_option("--action", help="Specify the action you want to carry out, OPEN for opening firewall, CLOSE for stopping publishing", metavar="action", default="CLOSE")
parser.add_option("--name", help="Specify the name of the Engineer (firstNameLastName), running the script", metavar="name", default="JohnDoe")
parser.add_option("--rfc", help="Specif the RFC number for this change", metavar="rfc", default="00000")
(options, args) = parser.parse_args()

# Define Local Variables
action = options.action
engineerName = options.name
rfc = options.rfc

# Massaging the variables
logPreFix = engineerName +" : " + rfc +" :"
action = action.upper()

if (engineerName == 'JohnDoe' or rfc == 00000):
        print "No engineer name or RFC specified, please try again"
        sys.exit()
else:
        if (action == 'OPEN'):
                logToSyslog(logPreFix,"Closing Firewall")
                firewallFlush()
                saveFirewallState()
                sys.exit()
        elif (action == 'CLOSE'):
                prod4ServerList = generateServerNames(4)
                for server in prod4ServerList:
                        logToSyslog(logPreFix,"Opening access to :"+server)
                        firewallRuleChange(server)                
                prod5ServerList = generateServerNames(5)
                for server in prod5ServerList:
                        logToSyslog(logPreFix,"Opening access to :"+server)
                        firewallRuleChange(server)
                prod6ServerList = generateServerNames(6)
                for server in prod6ServerList:
                        logToSyslog(logPreFix,"Opening access to :"+server)
                        firewallRuleChange(server)
                saveFirewallState()
                sys.exit()
        else:
                print "Incorrection operation specified, the options are CLOSE/OPEN. Please try again"
                sys.exit()
