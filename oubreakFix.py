#!/usr/bin/env python
#
#outbreakFix.py: Script to check infected files and restore from backup

__author__      = "Vinay Kudithipudi"

#Importing modules
import string
import os


#Define Variables
backupDirectory = 'C:\Users\Samurai\Desktop\check'
infectedDirectory = 'C:\Users\Samurai\Desktop\check'

def correctFileName(string):
        """ Return correct file name based on infected filename """
        #Check if the file is infected first
        if (string.find(".scr") != -1):
                tempArray = string.split("?")
                tempFileNamePrefix = tempArray[0]
                tempFileNameSuffix = tempArray[1].split(".")[0][::-1]
                tempFileName = tempFileNamePrefix + "." + tempFileNameSuffix
                return tempFileName

def backupFile(string):
        """ Make a backup of the file name provided """
        inputFile = string
        outputFile = correctFileName(inputFile)
        outputFile = "BACKUP_OF_INFECTED_FILE_9_26_2012_" + outputFile
        command = "move " + "\"" + inputFile + "\"" + " " + "\"" + outputFile + "\""
        if outputFile:
                os.system(command)
                
infectedFiles = os.listdir(os.curdir)
for file in infectedFiles:
        originalFile = correctFileName(file)
        if originalFile:
                backupFile(file)

