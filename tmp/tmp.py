#!/usr/bin/python

import re

def main():
    filehandler = open('tmp.txt', 'r')
    print 'STATUS_CODE = {'
    for line in filehandler:
        match = re.match('(\d\d\d)\s(.+)', line)    
        if match:
            print '    ' + match.group(1)+":", '"' + match.group(2) + '",' 
    print '}'
if __name__ == '__main__':
    main()
