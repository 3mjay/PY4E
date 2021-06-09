# Revise a previous program as follows:
# Read and parse the “From” lines and pull out the addresses from the line.
# Count the number of messages from each person using a dictionary.
#
# After all the data has been read, print the person with the most commits by
# creating a list of (count, email) tuples from the dictionary.
# Then sort the list in reverse order and print out the person who has the most commits.
#
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
#
# Enter a file name: mbox.txt
# zqian@umich.edu 195

filename = input("Enter file name:")
fhand = open(filename)

emails = {}

for line in fhand:
    if line.startswith("From:"):
        email = line.split()[1]
        emails[email] = emails.get(email, 0) + 1

lst = list()

for k, v in list(emails.items()):
    lst.append((v, k))

lst.sort(reverse=True)
print(lst)




# filename = input("Enter file name: ")
# fhand = open(filename)
#
# emails = {}
#
# max_address = None
# max_emails = 0
#
# for line in fhand:
#     if line.startswith("From:"):
#         email = line.split()[1]
#         emails[email] = emails.get(email, 0) + 1
#
# # for email in emails:
# #     if emails[email] > max_emails:
# #         max_emails = emails[email]
# #         max_address = email
#
# lst = list()
#
# for k, v in list(emails.items()):
#     lst.append((v, k))
#
# lst.sort(reverse=True)
#
# print(lst)
