score = input('Enter score: ', )
try:
    fscore = float(score)
except:
    print('Bad score')
    quit()
if fscore > 1.0:
    print('Bad score')
elif fscore >= 0.9:
    print('A')
elif fscore >= 0.8 and fscore < 0.9:
    print ('B')
elif fscore >= 0.7 and fscore < 0.8:
    print ('C')
elif fscore >= 0.6 and fscore < 0.7:
    print ('D')
elif fscore < 0.6:
    print ('F')
elif fscore < 0.0:
    print('Bad score')
