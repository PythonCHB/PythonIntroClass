#!/usr/bin/env python

"""
sample of using while with break and continue and else
"""

def count_them(letter):
    count = 0
    while True:
        in_letter = raw_input("give me a letter (x to stop)")
        print "you gave me:", in_letter
        if in_letter == letter:
            count += 1
        
        if in_letter == 'x':
            break    
    print "there were:", count, "instances of the letter:", letter
    
    return count

def count_them2(string, letter):
    """
    counts the number of instances of the letter in the string
    
    ends when a period is encountered
    """
    count = 0
    for l in string:
        if l == '.':
            break
        if l == letter:
            count = count+1
    else:
        print "hey, there was no period!"
    return count

