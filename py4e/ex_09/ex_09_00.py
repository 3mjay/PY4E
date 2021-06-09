filename = input("Enter file name: ")
if len(filename) < 1: filename = "mbox.txt" #opens mbox file if press enter w/o input
fhand = open(filename)

di = dict()
for line in fhand:
    line = rstrip()
    wds = line.split()
    for w in wds:
        # idiom: retrieve/create/update/counter
        di[w] = di.get(w, 0) + 1

# now we want to find most common word
largest = -1
theword = None
for k,v in di.items():
    if v > largest :
        largest = v
        theword = k
print(theword, largest)
