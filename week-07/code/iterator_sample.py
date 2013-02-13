#!/usr/bin/env python

"""
Simple iterator examples
"""


class IterateMe_1(object):
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like range(4) )
    """
    def __init__(self, stop=5):
        self.current = 0
        self.stop = stop
    def __iter__(self):
        return self
    def next(self):
        if self.current < self.stop:
            self.current += 1
            return self.current
        else:
            raise StopIteration

class IterateMe_2(object):
    """
    Almost a replacement for xrange:
   
    Iterate_2 (start, stop, step=1)

    returns the sequence of numbers from start (inclusive) to stop (exclusive),
    skipping every step number
    ( like xrange(start, stop, step) )
    """
    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step
    def __iter__(self):
        return self
    def next(self):
        if self.current < self.stop:
            self.current += self.step
            return self.current
        else:
            raise StopIteration

class IterateMe_3(object):
    """
    Almost a replacement for xrange:
   
    Iterate_2 (start, stop, step=1)

    returns the sequence of numbers from start (inclusive) to stop (exclusive),
    skipping every step number
    ( like xrange(start, stop, step) )
    
    This version re-sets itself when used again.
    """
    def __init__(self, start, stop, step=1):
        self.current = self.start = start
        self.stop = stop
        self.step = step
    def __iter__(self):
        self.current = self.start
        return self
    def next(self):
        if self.current < self.stop:
            self.current += self.step
            return self.current
        else:
            raise StopIteration

class IterateMe(object):
    """
    a re-written xrange
    """
    def __init__(self, start, stop, step=1):
        self.start = self.current = start
        self.stop = stop
        self.step = step
    def __iter__(self):
        print "__iter__ called"
        #self.current = self.start # if you want to reset...
        return self
    def next(self):
        print "next called"
        current = self.current
        if current >= self.stop:
            raise StopIteration
        self.current += self.step
        return current
        
        

## hand-written for loop:
print "a hand_written for loop:"
x = range(5)

it = iter (x)
while True:
    try:
        i = it.next()
    except StopIteration:
        break
    # do the body of the loop
    print i

        
if __name__ == "__main__":
    
    print "first version"
    for i in IterateMe_1():
        print i

    print "second version"
    for i in IterateMe_2(0, 5):
        print i

    print "second version with as different start"
    for i in IterateMe_2(4, 7):
        print i

    print "second version with as different step"
    for i in IterateMe_2(4, 15, 3):
        print i

    print "But what if we break out of it:"
    it = IterateMe_2(2, 20, 2)
    for i in it:
        if i > 10:
            break
        print i

    print "And then pick up again"
    for i in it:
        print i

    print "This one is different when broken out of"
    it = IterateMe_3(2, 20, 2)
    for i in it:
        if i > 10:
            break
        print i

    print "we pick up again from the beginning"
    for i in it:
        print i


#    print "do another loop"
#    for i in my_iterator:
#        print i
#        #print "current:", my_iterator.current



