#!/usr/bin/env python

import cookielib
import urllib
import urllib2

ID_USERNAME = 'email'
ID_PASSWORD = 'password'

USERNAME = ''
PASSWORD = ''

LOGIN_URL = 'http://www.renren.com/'
NORMAL_URL = 'http://guide.renren.com/guide'

def extract_cookies_info():
	cj = cookielib.CookieJar()
	login_data = urllib.urlencode({ID_USERNAME : USERNAME,ID_PASSWORD : PASSWORD})
	print login_data
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	
	resp = opener.open(LOGIN_URL,login_data)
	
	for cookie in cj:
		print "--First time cookie: %s --> %s" %(cookie.name,cookie.value)
		
	#print "Headers: %s" %resp.headers
	
	resp = opener.open(NORMAL_URL)
	for cookie in cj:
		print "+++Second time cookie: %s --> %s" %(cookie.name,cookie.value)
		
	#print "Headers: %s" %resp.headers
	
if __name__ == '__main__':
	extract_cookies_info()
