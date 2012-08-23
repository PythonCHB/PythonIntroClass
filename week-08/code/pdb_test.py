#!/usr/bin/env python

"""
simple file to try out debugger
"""

import pdb

a = "aaa"

pdb.set_trace()

b = "bbb"
c = "ccc"
final = a + b + c
print final

