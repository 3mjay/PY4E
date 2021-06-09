# Add code to the above program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary has been created,
# look through the dictionary using a maximum loop
# (see Chapter 5: Maximum and minimum loops) to find who has the most messages
# and print how many messages the person has.
#
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
#
# Enter a file name: mbox.txt
# zqian@umich.edu 195




filename = input("Enter file name: ")
fhand = open(filename)

emails = {}

max_address = None
max_emails = 0

for line in fhand:
    if line.startswith("From:"):
        email = line.split()[1]
        emails[email] = emails.get(email, 0) + 1

for email in emails:
    if emails[email] > max_emails:
        max_emails = emails[email]
        max_address = email
print(max_address, max_emails)
