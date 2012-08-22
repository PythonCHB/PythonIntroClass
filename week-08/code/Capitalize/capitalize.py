#!/usr/bin/env python

"""
A really simple script just to demonstrate disutils
"""

import sys, os
import capital_mod


if __name__ == "__main__":
    infilename = sys.argv[1]
    root, ext = os.path.splitext(infilename)
    outfilename = root + "_cap" + ext
    
    # do the real work:
    print "Capitalizing: %s and storing it in %s"%(infilename, outfilename)
    capital_mod.capitalize(infilename, outfilename)
    
    print "I'm done"
    