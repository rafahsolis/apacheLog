#!/usr/bin/python
import lib.apacheLogStatslib as apacheLib
import os
import csv


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

def closeLog(siteLog):
    os.system('clear')
    del siteLog
    print 'Log closed'


def menu():
    option = None
    while option != 'q':
        print apacheLib.menuOptions
        option = raw_input('\nSelect option (q to quit): ')
 
        if option == '1':
            siteLog = loadLog()

        elif option == '2':
            generalStats(siteLog)
        elif option == '3':
            try:
                accessStats(siteLog)
            except:
                print 'You must load a log file first.'
        elif option == '4':
                print 'You must load a log file first.'
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
