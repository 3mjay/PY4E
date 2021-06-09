# Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.
fruit = "banana"
index = -1
count = 1
while count < len(fruit):
    count = count + 1
    index = index - 1
    print(fruit[index])
