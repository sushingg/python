#!/usr/bin/env python

import socket

def print_machine_info():
	host_name = socket.gethostname()
	ip_adress = socket.gethostbyname(host_name)
	print "Host name: %s" % host_name
	print "IP address: %s" % ip_adress

if __name__ == '__main__':
	print_machine_info()
