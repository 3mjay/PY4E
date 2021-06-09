shrs = input('Enter hours: ')
srte = input('Enter rate: ')
# converting string input to float
fhrs = float(shrs)
frte = float(srte)
# computing pay for hours worked
reg = fhrs * frte
otp = ( (40 * frte) + ( (fhrs-40) * (frte*1.5) ) )
# outputting results
if fhrs > 40:
    print ('Overtime Pay:', otp)
else:
    print('Regular Pay:', reg)

##commented out my first attempt
# pay = fhrs*frte
# othrs = (fhrs - 40)
# otrte = (1.5 * frte)
# otpay = (othrs*otrte) + (40*frte)
#
# if fhrs > 40:
#    print ('Overtime Pay:', otpay)
# else:
#    print('Regular Pay:', pay)
