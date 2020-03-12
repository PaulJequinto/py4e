def computepay(hours, rate) :
    #print("In computepay", hours, rate)
    if hours > 40 :
        reg = hours * rate
        ot = (hours - 40.0) * (rate * 0.5)
        print(reg, ot)
        pay = reg + ot
    else:
        pay= hours * rate
    #print("Returning", pay)
    return pay
a = float (input ("Enter Hours:"))
b = float (input ("Enter Rate:"))

xp = computepay (a,b)

print ("Pay:" + str(xp))
