# Write a program to read through a file and print the contents of the file (line by line) all in upper case.

# Executing the program will look as follows:
# python shout.py
# Enter a file name: mbox-short.txt
# FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
# RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
# RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
#      BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
#      SAT, 05 JAN 2008 09:14:16 -0500

# fname = input('Enter file name: ')
#
# try:
#     fhand = open(fname)
# except:
#     print('File can not be opened:', fname)
#     quit()
#
# count = 0
#
# for line in fhand:
#     if line.startswith('Subject: '):
#         count = count + 1
# print('There were', count, 'subject lines in', fname    )
#

fname = input('Enter file name: ')

try:
    fhand = open(fname)
except:
    print('The file,', fname + ',', 'can not be opened.')
    quit()

# BREAKS CODE
# rfile = fhand.read()
# print(rfile.upper())

count = 0

for line in fhand:
    if line.startswith('Subject: '):
        count = count + 1
print('There were', count, 'xyz lines in', fname)
