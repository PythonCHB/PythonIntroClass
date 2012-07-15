#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Unicode lab:

"""

##Find some nifty non-ascii characters you might use.
##Create a unicode object with them in two different ways.

# (same as the hello_unicode example)

hello = 'Hello '
# note utf-8 specification string at the top...
world = u'世界'

print hello + world

## here are ways to do it with straight ascii in the source file
print u"It was nice weather today: it reached 80\u00B0"
print u"Maybe it will reach 90\N{degree sign}"

## and again with a unicode literal
print u"It is extremely rare for it ever to reach 100° in Seattle"

print

## In the ”code” dir for this week, there are two files:
## text.utf16
## text.utf32
## read the contents into unicode objects

## the easiest way is to use the codecs module file object:
import codecs

f = codecs.open('text.utf16', 'r', encoding='utf16')
text = f.read()
print text
print # just to get a blank line

## or you can do the decoding by hand:

f = open('text.utf32', 'rb')
encoded_text = f.read()
text = codecs.decode(encoded_text, 'utf32', 'replace')

print text

## write some of the text from the first exercise to file. read that file back in.

