#!/usr/bin/python
import datetime
from settings import *
import os

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
        self.time = datetime.datetime.strptime(logLine[DATE_LOG_POS], '[%d/%b/%Y:%H:%M:%S')
        self.userAgent = logLine[USER_AGENT_POS]
        self.document = logLine[METHOD_DOC_POS]
        self.status_code = int(logLine[STATUS_CODE_POS])
        self.requested_document = None

        LogFile.addEntry(self)
        LogFile.IpFreqAdd(self.ip)

    def __str__(self):
        return '\nIP: ' + self.ip + '\n' + \
               'Datetime: ' + str(self.time) + '\n' + \
               'User Agent: ' + self.userAgent + '\n' + \
               'Document: ' + self.document + '\n' + \
               'Status Code: ' + str(self.status_code)

def logNotLoaded():
    os.system('clear')
    print MSG['Load Log Error']


welcomeMessage = '''                    Apache log analyzer
                    Rafael Herrero Solis'''

menuOptions = '''1) Load log file
2) View general stats
3) View IP stats
4) Select ip and view activity
5) Close log file
6) View status code >= 400'''


MSG ={
    'Load Log Error': '\n***ERROR***\nYou must load a log file firs.\n',
    'Menu Select': '\nSelect option (q to quit):',
    'Press Enter': '\nPress enter to continue...',
    'Enter Number': '\nEnter option number: ',
    'File Path': 'Input log file path: ',
    'Path error': 'Log file not found: '
}

STATUS_CODE = {
    100: 'Continue',
    101: 'Switching Protocols',
    102: 'Processing',
    200: 'OK',
    201: 'Created',
    202: 'Accepted',
    203: 'Non-Authoritative Information',
    204: "No Content",
    205: "Reset Content",
    206: "Partial Content",
    207: "Multi-Status (WebDAV; RFC 4918)",
    208: "Already Reported (WebDAV; RFC 5842)",
    226: "IM Used (RFC 3229)",
    300: "Multiple Choices",
    301: "Moved Permanently",
    302: "Found",
    303: "See Other (since HTTP/1.1)",
    304: "Not Modified",
    305: "Use Proxy (since HTTP/1.1)",
    306: "Switch Proxy",
    307: "Temporary Redirect (since HTTP/1.1)",
    308: "Permanent Redirect (RFC 7538)",
    400: "Bad Request",
    401: "Unauthorized",
    402: "Payment Required",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    407: "Proxy Authentication Required",
    408: "Request Timeout",
    409: "Conflict",
    410: "Gone",
    411: "Length Required",
    412: "Precondition Failed",
    413: "Request Entity Too Large",
    414: "Request-URI Too Long",
    415: "Unsupported Media Type",
    416: "Requested Range Not Satisfiable",
    417: "Expectation Failed",
    418: "I'm a teapot (RFC 2324)",
    419: "Authentication Timeout (not in RFC 2616)",
    420: "Method Failure (Spring Framework) / Enhance Your Calm (Twitter)",
    422: "Unprocessable Entity (WebDAV; RFC 4918)",
    423: "Locked (WebDAV; RFC 4918)",
    424: "Failed Dependency (WebDAV; RFC 4918)",
    426: "Upgrade Required",
    428: "Precondition Required (RFC 6585)",
    429: "Too Many Requests (RFC 6585)",
    431: "Request Header Fields Too Large (RFC 6585)",
    440: "Login Timeout (Microsoft)",
    444: "No Response (Nginx)",
    449: "Retry With (Microsoft)",
    450: "Blocked by Windows Parental Controls (Microsoft)",
    451: "Unavailable For Legal Reasons (Internet draft) / Redirect (Microsoft)",
    494: "Request Header Too Large (Nginx)",
    495: "Cert Error (Nginx)",
    496: "No Cert (Nginx)",
    497: "HTTP to HTTPS (Nginx)",
    498: "Token expired/invalid (Esri) / Client Closed Request (Nginx)",
    499: "Token required (Esri)",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
    505: "HTTP Version Not Supported",
    506: "Variant Also Negotiates (RFC 2295)",
    507: "Insufficient Storage (WebDAV; RFC 4918)",
    508: "Loop Detected (WebDAV; RFC 5842)",
    509: "Bandwidth Limit Exceeded (Apache bw/limited extension)[29]",
    510: "Not Extended (RFC 2774)",
    511: "Network Authentication Required (RFC 6585)",
    598: "Network read timeout error (Unknown)",
    599: "Network connect timeout error (Unknown)"
}