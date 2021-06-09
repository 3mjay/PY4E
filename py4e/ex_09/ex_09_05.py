# This program records the domain name (instead of the address)
# where the message was sent from instead of who the mail came from
# (i.e., the whole email address). At the end of the program,
# print out the contents of your dictionary.
#
# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}




filename = input("Enter file name: ")
fhand = open(filename)

emails = {}

max_address = None
max_emails = 0

for line in fhand:
    if line.startswith("From:"):
        # print(line.split(delimiter)[1])
        email = line.rstrip().split("@")[1]
        emails[email] = emails.get(email, 0) + 1

print(emails)
# for email in emails:
#     if emails[email] > max_emails:
#         max_emails = emails[email]
#         max_address = email
# print(max_address, max_emails)
#print(emails)
