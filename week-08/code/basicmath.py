#!/usr/bin/env python


#############################
def logged_add(a, b):
    print '### %s(%r, %r)' % ('add', a, b)
    result = add(a, b)
    print '### %s(%r, %r) --> %r' % ('add', a, b, result)
    return result

# could change all calls to this... bleh




#############################
def logged(func):
    def wrapper(a, b):
        print '### %s(%r, %r)' % (func.func_name, a, b)
        result = func(a, b)
        print '### %s(%r, %r) --> %r' % (func.func_name, a, b, result)
        return result
    return wrapper


#############################
def logged(func):
    def wrapper(*args):
        print '### %s(%s)' % (func.func_name, args)
        result = func(*args)
        print '### %s(%s) --> %r' % (func.func_name, args, result)
        return result
    return wrapper



#============================

def add(a, b):
    """add() adds things"""
    return a + b
add = logged(add)

def subtract(a, b):
    """subtract() subtracts two things"""
    return a - b
subtract = logged(subtract)

def even(a):
    """even() returns True if the value is even"""
    return a % 2 == 0
even = logged(even)


if __name__ == "__main__":
    print '--- calling some math functions'
    add(1, 1)
    #logged_add(1,1)
    
    add(2, 2)
    
    subtract(2, 1)
    
    even(42)
    print '--- end'
