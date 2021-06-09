def count(string, letter):
    word = string
    count = 0
    for alphabet in word:
        if alphabet == letter:
            count = count + 1
    print(count)

count("banana", "a")
