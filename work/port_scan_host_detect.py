#!/usr/bin/env python
from socket import *

if __name__ == '__main__':
        port445=0
        port135=0
        target = raw_input("Enter host to scan: ")
        targetIP = gethostbyname(target)
        print 'Starting scan on host ',targetIP
        for i in range(20, 1025):
                s = socket(AF_INET,SOCK_STREAM)
                result = s.connect_ex((targetIP, i))
                print 'scanning on port',i
                if(result == 0):
                        print 'Port %d: OPEN' %(i)
                        print
                        if (i == 135):
                                port135 = 1
                        if (i == 445):
                                port445 = 1

                s.close()

        if(port135 == 1 and port445 == 1):
                print 'os:Windows'
        else:
                print 'os:Unknow'
                
        
                      
