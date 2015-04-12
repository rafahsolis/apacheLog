#!/usr/bin/python
import lib.apacheLogStatslib as apacheLib
import os
from time import sleep


def loadLog():
    logFileName = raw_input('Input log file path: ')

    try:
        logFile = open(logFileName, 'r')
    except:
        print 'Log file not found: ', logFileName

    for line in logFile:
        print line


def menu():
    option = None
    while option != 'q':
        print apacheLib.menuOptions
        option = raw_input('\nSelect option (q to quit): ')
 
        if option == '1':
            loadLog()
        

def main():
    print apacheLib.welcomeMessage
    os.system('clear')
    menu()


if __name__ == '__main__':
    main()
