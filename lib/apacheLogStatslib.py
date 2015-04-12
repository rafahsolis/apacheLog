#!/usr/bin/python
import datetime
from settings import *


class LogFile():
    def __init__(self):
        self.ip_freq = {}
        self.entryData =[]

    def addEntry(self, entry):
        self.entryData.append(entry)

    def IpFreqAdd(self, entry):
        self.ip_freq[entry] = self.ip_freq.get(entry, 0) + 1


class Entry():
    def __init__(self, LogFile, logLine):
        self.lineList = logLine

        self.ip = logLine[IP_LOG_POS]
        self.time = logLine[DATE_LOG_POS]
        self.userAgent = None
        self.document = None
        self.status_code = None
        self.requested_document = None

        LogFile.addEntry(self)
        LogFile.IpFreqAdd(self.ip)


welcomeMessage = '''                    Apache log analyzer
                    Rafael Herrero Solis'''

menuOptions = '''1) Load log file
2) View general stats
3) View IP stats
4) Select ip and view activity
5) Close log file'''