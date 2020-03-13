tl = 0.0
sa = input ("Enter a number: ")
nm = float(sa)
minimum = nm
maximum = nm

while True :
  sa = input("Enter a number: ")
  if sa == "done" :
        break
  try:
        nm = float(sa)
        if nm > maximum:
            maximum = nm
        if nm < minimum:
            minimum = nm

  except:
        print("Invalid input")
        continue
  #print (f)
nm = nm + 1


print ("All Done")
print (tl, nm,)
print ("Max: " + str(maximum))
print ("Min: " + str(minimum))
