#!/usr/bin/env python

"""
samples of using while and for with break, continue, and else
"""

def count_them(letter):
    """
    prompts the user to input a letter
    
    counts the number of times the given letter is input
    
    continues until the user inputs "x"
    
    returns the count of the letter input
    """
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


def count_letter_in_string(string, letter):
    """
    counts the number of instances of the letter in the string
    
    ends when a period is encountered
    
    if no period is encountered -- prints "hey, there was no period!"
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

