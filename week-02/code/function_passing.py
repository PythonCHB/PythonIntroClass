#!/usr/bin/env python

def simple():
    print "I'm simple"

def run_twice(fun):
    fun()
    fun()

run_twice( simple )
vs.
run_twice( simple() )