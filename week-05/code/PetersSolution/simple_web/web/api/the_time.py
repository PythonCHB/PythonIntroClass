#!/usr/bin/env python

import sys
import time

def do_time_date():
    time_date = time.strftime( "%m/%d/%Y - %H:%M:%S" )
    output = ["<html><head><title>the_time.py</title></head>",]
    output.append( "<body><p>The Current Date and Time is <b>%s<b></p></body></html>" % ( time_date ) )
    print "".join( output )

if __name__ == "__main__":
    do_time_date()
    sys.exit( 0 )