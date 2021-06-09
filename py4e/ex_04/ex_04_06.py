# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print("I sleep all night and I work all day.")
#
# print_lyrics()
#
# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()
#
# repeat_lyrics()
#
# def addtwo(a, b):
#     added = a + b
#     return added
#
# x = addtwo(3,5)
# print(x)
#
######################################################################
string_hours = input('Enter hours: ')
try:
    float_hours = float(string_hours)
    string_rate = input('Enter rate: ')
    float_rate = float(string_rate)
except:
    print ('Error, please enter numeric input')
    quit()

# converting string input to float
float_hours = float(string_hours)
float_rate = float(string_rate)

def computepay(hours, rate):
    # computing pay for hours worked
    reg = hours * rate
    otp = ( (40 * rate) + ( (hours-40) * (rate*1.5) ) )
    # outputting results
    if hours > 40:
        print ('Overtime Pay:', otp)
    else:
        print('Regular Pay:', reg)

pay = computepay(float_hours, float_rate)
