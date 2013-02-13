#!/usr/bin/env python

import sys

def do_echo_test( args ):
    print "<html><head><title>Test.py</title></head><body><h2>My Args Are: %s</h2></body></html>" % ( str( args ) )

if __name__ == "__main__":
    do_echo_test( sys.argv[1:] )
    sys.exit( 0 )