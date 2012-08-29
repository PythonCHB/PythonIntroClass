#!/usr/bin/env python

"""
circle class -- my solution to the exercise

This version with doctests...

"""

import math

class Circle(object):
    """
    A class that defines a circle.
    
    You can get and set either the radius or the diameter with properties. Example:
    
    >>> c = Circle(4)
    >>> c.radius
    4.0
    >>> c.diameter
    8.0
    >>> c.diameter = 4
    >>> c.radius
    2.0
    >>> c.area
    12.566370614359172
    >>> c2 = Circle(6)
    >>> c + c2
    Circle(8.000000)
    >>> str(c2)
    'Circle Object with radius: 6.000000'
    >>> 
    """
    def __init__(self, radius):
        self.radius = float(radius)
    
    @property
    def diameter(self):
        return self.radius * 2.0
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2.0

    @property
    def area(self):
        return self.radius**2 * math.pi
    
    def __add__(self, other):
        return Circle(self.radius + other.radius)
    
    def __repr__(self):
        return "Circle(%f)"%self.radius

    def __str__(self):
        return "Circle Object with radius: %f"%self.radius

if __name__ == "__main__":
    import doctest
    print doctest.testmod()