#!/usr/bin/env python

import sys

def do_add( args ):
    total = 0
    if ( len( args ) > 1 ):
        for x in args:
            try:
                x = int( x )
                total += x
            except:
                pass # Ignore non numbers
        print "<html><head><title>Add.py</title></head><body><p>%s = %d</p></body></html>" % ( " + ".join( args ), total )
    else:
        print "<html><head><title>Add.py</title></head><body><p>Pass one or more arguments via the uri in the format Add.py?1&4&5&2</p></body></html>"

if __name__ == "__main__":
    do_add( sys.argv[1:] )
    sys.exit( 0 )