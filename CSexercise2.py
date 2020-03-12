try:
    a = float(input("Enter Hours: "))
    b = float(input("Enter Rate: "))
except:
    print("Error, please enter numeric input")
    quit()
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
