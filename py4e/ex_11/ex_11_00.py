# import re
#
# line = "From stephen.marquard@uct.ac/za Sat Jan  5 09:14:16 2008"
#
# # words = line.split()[1]
# # print(words.split('@')[0])
#
# #regex extraction:
# #looks for '@', once found extracts non whitespace character many times
#
# # y = re.findall('@([\S]*)', line)
# # print(y)
#
#
# #regex extraction:
# #looks for string that starts with 'From ', followed by many characters,
# #followed by '@'.once found,extracts nonblank character many times
#
# y = re.findall('^From .*@([^ ]*)', line)
# print(y)

import re

hand = open('mbox-short.txt')

numlist = list()

for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([^ ]*)', line)
    #better regex b/c it looks specifically for #s b/w 0-9 including '.'
    #stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print("Maximum:",max(numlist))
