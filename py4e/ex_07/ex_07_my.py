while True:
    count = 0
    fpoint = 0
    fname = input("Enter file name: ")
    try:
        fhand = open(fname)
    except:
        if fname == "na na boo boo":
            print("StOp mOcKiNg MeEmeMEEE!!!\nType 'quit' to exit.")
            continue
        elif fname == "quit":
                quit()
        print("The file:", fname, "can not be opened.\nType 'quit' to exit.")
        continue
    for line in fhand:
        if line.startswith('X-DSPAM-Confidence:'):
            fpoint = fpoint + float(line[20:])
            count = count + 1
    print('Average spam confidence:', fpoint/count)
    quit()


# **************************BREAKS CODE*****************************************
# rfile = fhand.read()
# print(rfile)
# print(rfile.upper())
# Look for X-DSPAM-Confidence: 0.8475
