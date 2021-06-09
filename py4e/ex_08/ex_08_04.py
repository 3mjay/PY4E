# Write a program to open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split function.
# For each word, check to see if the word is already in a list.
# If the word is not in the list, add it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
#
# Enter file: romeo.txt
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
# 'and', 'breaks', 'east', 'envious', 'fair', 'grief',
# 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
# 'sun', 'the', 'through', 'what', 'window',
# 'with', 'yonder']

fname = input("Enter file name: ")

fhand = open(fname)
words = []

for line in fhand:
    for word in line.split():
        if word not in words:
            words.append(word)

# BREAKS CODE
#print(words.sort())

words.sort()
print (words)
#print(type(fname))
# print(fhand.split())
# for line in fhand:
#     fhand.split()




# fname = input('Enter file name: ')
#
# try:
#     fhand = open(fname)
# except:
#     print('The file,', fname + ',', 'can not be opened.')
#     quit()
# count = 0
# fpoint = 0
#
# for line in fhand:
#     if line.startswith('X-DSPAM-Confidence:'):
#         fpoint = fpoint + float(line[20:])
#         count = count + 1
#
# print('Average spam confidence:', fpoint/count)
# #**my code**##
# while True:
#     count = 0
#     fpoint = 0
#     fname = input("Enter file name: ")
#     try:
#         fhand = open(fname)
#     except:
#         if fname == "na na boo boo":
#             print("StOp mOcKiNg MeEmeMEEE!!!\nType 'quit' to exit.")
#             continue
#         elif fname == "quit":
#                 quit()
#         print("The file:", fname, "can not be opened.\nType 'quit' to exit.")
#         continue
#     for line in fhand:
#         if line.startswith('X-DSPAM-Confidence:'):
#             fpoint = fpoint + float(line[20:])
#             count = count + 1
#     print('Average spam confidence:', fpoint/count)
#     quit()
