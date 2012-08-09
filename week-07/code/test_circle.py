#!/usr/bin/env python

"""
code that tests the circle class defined in circle.py

When run, should result in:

the radius: 4
the diameter: 8
the area: 50.2654824574
the repr(): Circle(4.000000)
the str(): Circle Object with radius: 4.000000

setting the radius to 2:
the radius: 2
the diameter: 4
the area: 12.5663706144

setting the diameter to 6:
the radius: 3.0
the diameter: 6.0
the area: 28.2743338823

trying to delete the diameter
Whoops: can't delete attribute

trying to set the area
Whoops: can't set attribute

adding two circles together
Circle Object with radius: 6.000000

"""

from circle import Circle

print "creating a Circle with radius 4"    
c = Circle(4)
print "the radius:", c.radius    
print "the diameter:", c.diameter
print "the area:", c.area
print "the repr():", repr(c)
print "the str():", str(c)

print
print "setting the radius to 2:"
c.radius = 2
print "the radius:", c.radius    
print "the diameter:", c.diameter
print "the area:", c.area

print
print "setting the diameter to 6:"
c.diameter = 6
print "the radius:", c.radius    
print "the diameter:", c.diameter
print "the area:", c.area

print
print "trying to delete the diameter"
try:
    del c.diameter
except Exception as err:
    print "Whoops:", err
    
print
print "trying to set the area"
try:
    c.area = 40.0
except Exception as err:
    print "Whoops:", err

c1 = Circle(2)
c2 = Circle(4)
 
print
print "adding two circles together"
print c1 + c2
