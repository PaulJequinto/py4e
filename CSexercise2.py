a = input("Enter Hours: ")
try:
    c = float(a)
    b = input("Enter Rate: ")
    try:
         d = float(b)
    except:
        print("Error, please enter numeric input")
except:
    print("Error, please enter numeric input")

a = input("Enter Hours: ")
try:
    c = float(a)
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
