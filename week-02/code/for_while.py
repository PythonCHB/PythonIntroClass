#!/usr/bin/env python

"""
examples of while and for loops
"""

print "breaking out of a while loop"
x = 0
while True:
    print x
    if x > 3:
        break
    x = x + 1

print "breaking out of a for loop"
name = "Chris Barker"
for c in name:
    print c,
    if c == "B":
        break
print "\nI'm done"
    

print "continue in a for loop"
name = "Chris Barker"
for c in name:
    if c == "B":
        continue
    print c,
print "\nI'm done"

print "continue in a while loop"
x = 6
while x > 0:
    x = x-1
    if x%2:
        continue
    print x, 
print "\nI'm done"

print "else in a for loop"
x = 5
for i in range(5):
    print i
    if i == x:
        break
else:
    print "else block run"


