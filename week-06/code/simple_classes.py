#!/usr/bin/env python
"""
simple_classes.py

demonstrating the basics of a class
"""

## create a point class
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

## create an instance of that class        
p = Point(3,4)

## access the attributes
print "p.x is:", p.x
print "p.y is:", p.y