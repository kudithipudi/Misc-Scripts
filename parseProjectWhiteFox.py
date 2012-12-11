#!/usr/bin/env python
#
# parseProjectWhiteFox.py: Script parses the http URLs from ProjectWhiteFox release
# http://pastebin.com/agUFkEEa

__author__      = "Vinay Kudithipudi"

#Importing modules
import re
import string
import os
import glob
import fileinput
import urllib
import uuid
import time
import random


#Define Variables
fileParse="projectwhitefox.txt"

def find_urls(string):
    """ Extract all URL's from a string & return as a list """
    """ Credit to http://www.noah.org/wiki/RegEx_Python """
    url_list = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',string)
    return url_list

def convert_privatepaste_url(string):
    """ Convert the privatepate URL to downloadable format """
    head, sep, tail = string.rpartition('/')
    return_url = head + '/download/' + tail
    return return_url

def convert_pastesite_url(string):
    """ Convert the pastesite URL to downloadable format """
    head, sep, tail = string.rpartition('/')
    return_url = head + '/plain/' + tail + '.txt'
    return return_url

def download_file(string,url):
    """ Download url """
    fileName = string.replace('/','_')
    fileName = fileName.replace(':',"_")
    urllib.urlretrieve(url, fileName)
    

inputFile = open(fileParse)
for eachLine in inputFile:
    if re.search("http", eachLine):
        parse1 = eachLine.split('-', 1)
        compromised = parse1[0]
        if (len(parse1) > 1):
            compromisedURLs = parse1[1]
            urls = find_urls(compromisedURLs)
            for url in urls:
                if 'privatepaste.com' in url:
                    fixed_url = convert_privatepaste_url(url)
                    print (compromised + ": " + fixed_url)
                    download_file(fixed_url, fixed_url)
