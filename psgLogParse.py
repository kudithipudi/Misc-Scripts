#!/usr/bin/env python
#
#psgLogParse.py: Script to parse PSG Files and create CSV files for graphing

__author__      = "Vinay Kudithipudi"

#Importing modules
import string
import os


#Define Variables
inputFiles = ['pil-vm-psg-11.log',
              'pil-vm-psg-12.log',
              'pil-vm-psg-21.log',
              'pil-vm-psg-22.log']


def parseLine(string):
        """ Take line from source file as input """
        """ and returns the server name, date, time and response time """
        tempArray = string.split(" ")
        tempArray2 = tempArray[0].split(":")
        tempArray3 = tempArray[1].split(",")
        tempString = tempArray2[1] + "," + tempArray3[0] + "," + tempArray[10]
        return tempString

             
for inputFile in inputFiles:
        openInputFile = open(inputFile)
        openOutputFile = open("parsed_"+inputFile,'w')
        for line in openInputFile:
                openOutputFile.write(parseLine(line)+"\n")
                print inputFile + "," + parseLine(line)
        openOutputFile.close
