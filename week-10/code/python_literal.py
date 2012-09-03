#!/usr/bin/env python

"""
Example of how to save data as python literals in a py file

"""

outfilename = "literal_data.txt"

# get the data from the py file
from add_book_data import AddressBook

# save it as python literals:

outfile = open(outfilename, 'w')

outfile.write(str(AddressBook))

outfile.close()

## see if we can re-load it

data = open(outfilename, 'r').read()

AddressBook2 = eval(data)

if AddressBook2 == AddressBook:
    print "they are the same"

## try again with the pretty print version:
import pprint

outfilename = "literal_data_pretty.txt"

outfile = open(outfilename, 'w')

outfile.write(pprint.pformat(AddressBook))

outfile.close()

## see if we can re-load it
data = open(outfilename, 'r').read()

AddressBook2 = eval(data)

if AddressBook2 == AddressBook:
    print "pretty printed version is the same as well"
    