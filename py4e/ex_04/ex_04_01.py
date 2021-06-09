import math
print (math)

import random

for i in range(10):
    x = random.randint(5, 10)
    print (x)

random.randint(5, 10)

t = [1, 2, 3]

random.choice(t)

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

print_lyrics()

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3,5)
print(x)
