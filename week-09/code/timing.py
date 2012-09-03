#!/usr/bin/env python

"""
timing example
"""

def primes_stupid(N):
    """
    a really simple way to compute the first N prime numbers
    """
    primes = [2]
    i = 3
    while len(primes) < N:
        for j in range(2, i/2): # the "/2" is an optimization -- no point in checking even numbers
            if not i % j: # it's not prime
                break
        else:
            primes.append(i)
        i += 1

    return primes

if __name__ == "__main__":
    import timeit

    print "running the timer:"
    run_time = timeit.timeit("primes_stupid(5)",
                             setup="from __main__ import primes_stupid",
                             number=100000) # default: 1000000
    print "it took:", run_time