# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix.
# Ask the user to enter a regular expression and count the number of lines that matched the regular expression:
#
# $ python grep.py
# Enter a regular expression: ^Author
# mbox.txt had 1798 lines that matched ^Author
#
# $ python grep.py
# Enter a regular expression: ^X-
# mbox.txt had 14368 lines that matched ^X-
#
# $ python grep.py
# Enter a regular expression: java$
# mbox.txt had 4175 lines that matched java$

import re

hand = open('mbox.txt')

regex = input("Enter a regular expression: ")

lst = list()
count = 0

for line in hand:
    line = line.rstrip()
    stuff = re.search(regex, line)
    if stuff is None : continue
    count += 1
    lst.append(stuff)

#print(lst)
print("mbox.txt had",count,"lines that matched",regex)
