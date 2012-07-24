#!/usr/bin/env python

"""
httpdate.py

Module that provides a function that formats a date to the HTTP 1.1 spec

"""

import datetime

def httpdate(dt):
    """Return a string representation of a date according to RFC 1123
    (HTTP/1.1).
    
    :param dt" A python datetime object (in UTC (GMT) time zone)

    For example:  datetime.datetime.utcnow()

    """
    weekday = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][dt.weekday()]
    month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
             "Oct", "Nov", "Dec"][dt.month - 1]
    return "%s, %02d %s %04d %02d:%02d:%02d GMT" % (weekday, dt.day, month,
        dt.year, dt.hour, dt.minute, dt.second)

def httpdate_now():
    return httpdate( datetime.datetime.utcnow() )
    
if __name__ == "__main__":
    
    print "the HTTP 1.1 date string for now is:"
    print httpdate_now()