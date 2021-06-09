# Exercise 3: Write a program to read through a mail log,
# build a histogram using a dictionary to count how many messages have come from each email address,
# and print the dictionary.
#
# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,

filename = input("Enter file name: ")
fhand = open(filename)

emails = {}

for line in fhand:
    if line.startswith("From:"):
        email = line.split()[1]
        emails[email] = emails.get(email, 0) + 1

# for email in emails:
#     print(email,emails[email])
print(emails)
