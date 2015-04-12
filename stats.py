#!/usr/bin/python
import lib.apacheLogStatslib as apacheLib
import os
import csv
import datetime


def loadLog():
    siteLog = apacheLib.LogFile()
    logFileName = raw_input('Input log file path: ')

    if len(logFileName) < 1:
        logFileName = 'access.log'

    try:
        logFile = open(logFileName, 'r')
    except:
        print 'Log file not found: ', logFileName

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
    print ''

    return


def generalStats(siteLog):
    print 'WIP'
    # @ToDo: visits this year
    # @ToDo: visits this month
    # @ToDo: Visits this week
    # @ToDo: visits today



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
    opt = int(raw_input("Number: "))
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

    raw_input('Press enter to continue...')
    os.system('clear')


def menu():
    option = None
    while option != 'q':
        print apacheLib.menuOptions
        option = raw_input('\nSelect option (q to quit): ')
 
        if option == '1':
            siteLog = loadLog()

        elif option == '2':
            try:
                generalStats(siteLog)
            except:
                print 'You must load a log file first.'

        elif option == '3':
            try:
                accessStats(siteLog)
            except:
                print 'You must load a log file first.'

        elif option == '4':
            ipStats(siteLog)
            # print 'You must load a log file first.'
        elif option == '5':
            try:
                del(siteLog)
            except:
                closeLog(siteLog)
        else:
            os.system('clear')
        

def main():
    print apacheLib.welcomeMessage
    os.system('clear')
    menu()


if __name__ == '__main__':
    main()
