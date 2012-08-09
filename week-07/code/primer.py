import math

def intsum():  # 1 + 2 + 3 + 4 + 5...
    a = 0
    while True:
        yield (a * (a + 1)) / 2
        a += 1

def intsum2():  # 1 + 2 + 3 + 4 + 5...
    a = b = 0
    while True:
        yield b
        a += 1
        b = b + a

def dub():  # 1, 2, 4, 8, 16, 32, 64...
    a = 1
    while True:
        yield a
        a = a * 2

def fib():  # 1, 1, 2, 3, 5, 8, 13, 21, 34...
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

def prime():  # 2, 3, 5, 7, 11, 13, 17, 19, 23...
    a = 2
    while True:
        yield a
        p = False
        while not p:                    # while not prime
            a += 1                      # try the next integer
            p = True                    # assume it is prime...
            for x in xrange(2, int(math.floor(math.sqrt(a))) + 1):
                if a % x == 0:
                    p = False           # ...unless it isn't
                    break


if __name__ == "__main__":
    v = intsum()
    w = intsum2()
    x = dub()
    y = fib()
    z = prime()
    for i in range(101):
        print i, v.next(), w.next(), x.next(), y.next(), z.next()

# try x^2, x^3, counting by threes, x^e, counting by minus seven
