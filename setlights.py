#!/usr/bin/python
#
'''Gets POST input - should be valid JSON - feeds it as output to the monadic setlights executeable

Homepage and documentation: http://dev.moorescloud.com/

Copyright (c) 2012, Mark Pesce.
License: MIT (see LICENSE for details)'''

__author__ = 'Mark Pesce'
__version__ = '0.01.dev'
__license__ = 'MIT'

import sys, os, json, urllib2, tempfile
import cgi

awt_colors = dict( black=0x808080, blue=0x8080FF, cyan=0x80FFFF, darkGray=0x818181, gray=0x848484, 
green=0x80FF80, lightGray=0x8f8f8f, magenta=0xFF80FF, orange=0xFF9780, pink=0xFF90EF, 
red=0xFF8080, white=0xFFFFFF, yellow=0xFFFF80, BLACK=0x808080, BLUE=0x8080FF, CYAN=0x80FFFF, 
DARK_GRAY=0x818181, GRAY=0x848484,GREEN=0x80FF80, LIGHT_GRAY=0x8f8f8f, MAGENTA=0xFF80FF, 
ORANGE=0xFF9780, PINK=0xFF90EF, RED=0xFF8080, WHITE=0xFFFFFF, YELLOW=0xFFFF80 )

print "Content-type: text/html"
print
print

form = cgi.FieldStorage()

lj = form.getvalue('lights')
l = json.loads(lj)

tf = tempfile.NamedTemporaryFile()
#tf = open('test.dat', 'wb')

#print l['lights']
for  bulb in l['lights']:
	if bulb in awt_colors:
		#print "Got a match!"
		colorval = awt_colors[bulb]
	else:
		#print bulb[1:]
		colorval = int(bulb[1:], 16)
	
	tf.write("%6X\n" % (colorval,))
	tf.flush()
#print "Name %s" % tf.name
os.system("""cat %s | /srv/http/cgi-bin/setlights""" % (tf.name))
tf.close()