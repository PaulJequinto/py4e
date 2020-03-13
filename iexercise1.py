nm = 0
tl = 0.0
while True :
  sa = input("Enter a number: ")
  if sa == "done" :
        break
  try:
        f = float(sa)
  except:
        print("Invalid input")
        continue
  #print (f)
nm = nm + 1
tl = tl + f

#print ("All Done")
print (tl, nm, tl/nm)
