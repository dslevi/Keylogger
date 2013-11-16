#!/usr/bin/python

import logMaker, analyze
import random, datetime

#changing depending on the user
user = random.randint(100, 999)
#find the right port for the user's computer/keyboard
port = 7
#hide this?
directory = "/var/log/keylogs/"
path = directory + str(user) + "date" + str(datetime.datetime.now()) + ".txt"

if (logMaker.createLog(port, path, directory)):
    profile = analyze.analyzeLog(path)
