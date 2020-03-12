a = float (input ("Enter Hours:"))
b = float (input ("Enter Rate:"))
if a > 40 :
    print("Overtime")
    reg = a * b
    ot = (a - 40.0) * (b * 0.5)
    print(reg, ot)
    xp = reg + ot
else:
    print("Regular")
print ("Pay:" + str(xp))
