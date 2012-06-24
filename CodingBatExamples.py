#!/usr/bin/env python

"""
CodingBat Examples:
"""

##Warmup-1 > sleep_in

#sample 1:
def sleep_in(weekday, vacation):
    if vacation:
        return True
    if not weekday:
        return True
    return False

#sample 2:
def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False 

#sample 3:
def sleep_in(weekday, vacation):
    # parentheses not required...
    return (not weekday) or vacation

## Warmup-1 > diff21:

def diff21(n):
    result = n - 21
    if result > 0:
        return result * 2
    else:
        return -result

## Warmup-1 > makes10:

def makes10(a, b):
    return a == 10 or b == 10 or a+b == 10

