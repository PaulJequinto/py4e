a = float(input ("Enter Hours:"))
#this is fh
b = float(input ("Enter Rate:"))
#this is fr
if a > 40 :
    print("Overtime")
    reg = a * b
    ot = (a - 40.0) * (b * 0.5)
    print(reg, ot)
    xp = reg + ot
else:
    print("Regular")
    #print regular
print ("Pay:" + str(xp))
