# Why should you learn to write programs? 7746
# 12 1929 8827
# Writing programs (or programming) is a very creative
# 7 and rewarding activity.  You can write programs for
# many reasons, ranging from making your living to solving
# 8837 a difficult data analysis problem to having fun to helping 128
# someone else solve a problem.  This book assumes that
# everyone needs to know how to program ...
#
#
# The sum for the sample text above is 27486.

import re

hand = open('sample.txt')

numbers = list()

for line in hand:
    line.rstrip()
    for i in line:
        stuff = re.findall('([0-9]+)', line)
        if len(stuff) != 1 : continue
    for x in stuff:
        nums = float(x)
        numbers.append(nums)
print("len:", len(numbers))
print("sum:", sum(numbers))


## can be made into 2 lines
# Python 2
# import re
# print sum( [ ****** *** * in re.findall('[0-9]+'),sample-txt.read()) ] )
#
# Python 3:
# import re
# print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
