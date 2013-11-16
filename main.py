#!/usr/bin/python

import logMaker, analyze
import random

#changing depending on the user
user = random.randint(100, 999)
#find the right port for the user's computer/keyboard
port = 7
#hide this?
directory = "/var/log/keylogs/"

if (logMaker.createLog(port, str(user), directory)):
    f = open(directory + str(user) + "log.txt", "r")
    log = f.read()
    f.close()
    profile = analyze.analyzeLog(log)
