#!/usr/bin/env python

"""
code for testing profiling

borrowed from:

http://pysnippet.blogspot.com/2009/12/profiling-your-python-code.html
"""

def odd_numbers(max):
    """ Returns a list with all odd numbers between 0 to max (inclusive) """
    l = list()
    for i in xrange(max+1):
        if (i & 1):
            l.append(i)
    return l

def sum_odd_numbers(max):
    """ Sum all odd numbers between 0 to max (inclusive) """
    odd_nbrs = odd_numbers(max)

    res = 0
    for odd in odd_nbrs:
        res += odd
    return res

def main():
    # Run this 100 times to make it measurable
    for i in xrange(100):
        print sum_odd_numbers(1024)

if __name__ == '__main__':
    main()

