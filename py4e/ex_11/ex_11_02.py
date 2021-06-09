#Exercise 2: Write a program to look for lines of the form:
#
#New Revision: 39772
#
# Extract the number from each of the lines using a regular expression and the findall() method.
# Compute the average of the numbers and print out the average as an integer.
#
# Enter file:mbox.txt
# 38549
#
# Enter file:mbox-short.txt
# 39756

import re

hand = open('mbox.txt')

#regex = input("Enter a regular expression: ")

lst = list()
# count = 0
numlist = list()
count = 0

for line in hand:
    line = line.rstrip()
    stuff = re.findall('^New Revision: ([0-9]+)', line)
    #stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)

    if len(stuff) != 1 : continue
    count += 1
    num = int(stuff[0])
    lst.append(num)
print(sum(lst)/len(lst))
# for i in lst:
#     print("New Revision: ",i)
#     count += 1
#     lst.append(stuff)
#
# #print(lst)
# print("mbox.txt had",count,"lines that matched",regex)
