#/usr/bin/ev python

"""
Trigram.py

A solution to the trigram coding Kata:

http://codekata.pragprog.com/2007/01/kata_fourteen_t.html
"""
infilename = "sherlock_small.txt"
#infilename = "sherlock.txt"

import string

# translation table for string.translate:
# stuff I want to keep:
valid = string.letters + "'"
all = ''.join([chr(i) for i in range(256)])
table = []
for c in all:
    if c in valid:
        table.append(c)
    else:
        table.append(' ')
table = ''.join(table)

# read it all into memory

#in_data = open(infilename, 'r').read()
in_data = open(infilename, 'r').read()
# Dictionary for results:
word_pairs = {}

# lower-case everything to remove that complication:
in_data = in_data.lower()
# strip out the punctuation:
in_data = in_data.translate(table)

#split into words (what about punctuation?)
words = in_data.split()# loop through the words
for i in range(len(words) - 2):
    pair = " ".join(words[i:i+2])
    follower = words[i+2]
    if pair in word_pairs:
        print "pair is repeated:", pair
        word_pairs[pair].append(follower)
    else:
        word_pairs[pair] = [follower]

# create some new text

import random
new_text = []        
for i in range (10): #just do a few
    pair = random.sample(word_pairs, 1)   
    

print word_pairs     