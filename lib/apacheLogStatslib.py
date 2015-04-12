#!/usr/bin/python

class LogFile():
    ip_freq = {}
    ipData =[]

class Entry():
    def __init__(logLine):
        self.ip = None
        self.time = None
        self.userAgent = None
        self.document = None
        self.status_code = None
        self.requested_document = None
        

       lineList = logLine.split()
       print lineList


welcomeMessage = '''                    Apache log analyzer
                    Rafael Herrero Solis'''
menuOptions = '''1) Load log file
2) View general stats
3) View IP stats
4) Select ip and view activity'''
