#!/usr/bin/env python
#$pip install ntplib   　$sudo apt-get install python-pip

import ntplib
from time import ctime

def print_time():
	ntp_client = ntplib.NTPClient()
	response = ntp_client.request('ntp.sjtu.edu.cn')
	print ctime(response.tx_time)
#	print response.tx_time

if __name__ == '__main__':
	print_time()





