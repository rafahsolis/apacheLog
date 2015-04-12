#!/usr/bin/python
import lib.apacheLogStatslib as apacheLib
import os
import csv
import datetime
TODAY = datetime.datetime.now().date()

def loadLog():
    siteLog = apacheLib.LogFile()
    logFileName = raw_input(apacheLib.MSG['File Path'])

    if len(logFileName) < 1:
        logFileName = 'access.log'

    try:
        logFile = open(logFileName, 'r')
    except:
        print apacheLib.MSG['Path error'], logFileName

    fileReader = csv.reader(logFile, delimiter=' ')
    for line in fileReader:
        NewEntry = apacheLib.Entry(siteLog, line)

    os.system('clear')
    print logFileName, ' Loaded\n'

    return siteLog


def accessStats(siteLog):
    os.system('clear')
    print 'Requests\tIP'
    sortedList = sorted([(v, k) for k, v in siteLog.ip_freq.items()], reverse=True)
    for value, ip in sortedList:
        print value, '\t', ip
    raw_input(apacheLib.MSG['Press Enter'])
    os.system('clear')
    return


def visitsThisYear(siteLog):

    yearEntrys = []
    # @ToDo: Show more info about visits
    for entry in siteLog.entryData:
        if TODAY.year == entry.time.year:
            yearEntrys.append(entry)
    print 'Total entrys year', TODAY.year, len(yearEntrys)


def visitsThisMonth(siteLog):

    monthEntrys = []
    # @ToDo: Show more info about visits
    for entry in siteLog.entryData:
        if TODAY.month == entry.time.month:
            monthEntrys.append(entry)
    print 'Total entrys month', TODAY.month, len(monthEntrys)


def visitsThisWeek(siteLog):
    weekEntrys = []
    for entry in siteLog.entryData:
        if TODAY.isocalendar()[1] == entry.time.isocalendar()[1]:
            weekEntrys.append(entry)
    print "Total entrys week", TODAY.isocalendar()[1], len(weekEntrys)


def visitsToday(siteLog):
    dayEntrys = []
    for entry in siteLog.entryData:
        if entry.time.month == TODAY.month and entry.time.day == TODAY.day and entry.time.year == TODAY.year:
            dayEntrys.append(entry)

    print "Total entrys today: ", len(dayEntrys)



def generalStats(siteLog):
    os.system('clear')

    visitsThisYear(siteLog)
    visitsThisMonth(siteLog)
    # @ToDo: Visits this week
    visitsThisWeek(siteLog)
    visitsToday(siteLog)
    raw_input(apacheLib.MSG['Press Enter'])
    os.system('clear')


def closeLog(siteLog):
    os.system('clear')
    del siteLog
    print 'Log closed'


def selectIP(siteLog):
    os.system('clear')
    counter = 0
    print 'Select IP: '
    for ip in siteLog.ip_freq.keys():
        print "%d) %s" % (counter, ip)
        counter += 1

    # @ToDo Error control in ip number input
    opt = int(raw_input(apacheLib.MSG['Enter Number']))
    ip_option = siteLog.ip_freq.keys()[opt]
    return ip_option


def ipStats(siteLog):
    ip = selectIP(siteLog)
    ip_data = []

    for i in siteLog.entryData:
        if i.ip == ip:
            ip_data.append(i)

    os.system('clear')
    print 'Showing data for IP = ', ip
    print 'Access number= ', siteLog.ip_freq[ip]

    for i in ip_data:
        print '\n'
        print 'ip:', i.ip
        print 'time: ', i.time.strftime("%d-%b-%Y %H:%M:%S")
        print 'User Agent: ', i.userAgent
        print 'Status code: ', i.status_code, apacheLib.STATUS_CODE[i.status_code]
        print 'Document: ', i.document

    raw_input(apacheLib.MSG['Press Enter'])
    os.system('clear')


def viewErrors(siteLog):
    entryErrors = []

    for entry in siteLog.entryData:
        if entry.status_code >= 400:
            entryErrors.append(entry)
            print entry

    raw_input(apacheLib.MSG['Press Enter'])


def menu():
    option = None
    while option != 'q':
        print apacheLib.menuOptions
        option = raw_input(apacheLib.MSG['Menu Select'])
 
        if option == '1':
            siteLog = loadLog()

        elif option == '2':
            try:
                generalStats(siteLog)
            except:
                apacheLib.logNotLoaded()

        elif option == '3':
            try:
                accessStats(siteLog)
            except:
                apacheLib.logNotLoaded()

        elif option == '4':
            try:
                ipStats(siteLog)
            except:
                apacheLib.logNotLoaded()
        elif option == '5':
            try:
                del(siteLog)
                os.system('clear')
                print 'Log closed.'
            except:
                apacheLib.logNotLoaded()

        elif option == '6':
            viewErrors(siteLog)

        else:
            os.system('clear')
        

def main():
    print apacheLib.welcomeMessage
    os.system('clear')
    menu()


if __name__ == '__main__':
    main()
