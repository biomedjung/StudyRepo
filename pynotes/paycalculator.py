#This program calculate a perons

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
#try:
h = float(hrs)
r = float(rate)
#except:
    #print('Use Numbers, Please!')

if h > 40 :
    base = h * r
    over = (h - 40) * (r * 0.5)
    pay = base + over
else :
    pay = h * r

print(pay)
