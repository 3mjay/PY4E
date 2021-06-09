fname = input('Enter file name: ')

if fname == "na na boo boo":
    print('StOp mOcKiNg MeEmeMEEE!!!')
    quit()
else:
    try:
        fhand = open(fname)
    except:
        print('The file,', fname + ',', 'can not be opened.')
        quit()


# **************************BREAKS CODE*****************************************
# rfile = fhand.read()
# print(rfile)
# print(rfile.upper())

# Look for X-DSPAM-Confidence: 0.8475
count = 0
fpoint = 0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        fpoint = fpoint + float(line[20:])
        count = count + 1

print('Average spam confidence:', fpoint/count)
