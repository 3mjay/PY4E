# Write a program that reads a file and prints the letters
# in decreasing order of frequency. Your program should convert all the input
# to lower case and only count the letters a-z. Your program should not count
# spaces, digits, punctuation, or anything other than the letters a-z.
# Find text samples from several different languages and see how letter frequency
# varies between languages. Compare your results with the tables at
# https://wikipedia.org/wiki/Letter_frequencies.
filename = input("Enter file name:")
fhand = open(filename)
docu = fhand.read().lower()

alphabet = ("abcdefghijklmnopqrstuvwxyz")

letters = {}
ls = list()

for letter in docu:
    if letter in alphabet:
        letters[letter] = letters.get(letter, 0) + 1

for k, v in list(letters.items()):
    ls.append((k, v))
    ls.sort()

for h, k in ls: print(h, k)
