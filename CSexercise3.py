a=input("Enter score: ")
float(a)
try:
  if float(a) >= 0.9 and float(a) <= 1.0:
    print("A")
  elif float(a) >= 0.8 and float(a) <= 0.9:
    print("B")
  elif float(a) >= 0.7 and float(a) <= 0.8:
    print("C")
  elif float(a) >= 0.6 and float(a) <= 0.7:
    print("D")
  elif float(a) > 0 and float(a) <= 0.6:
    print("F")
  else:
    print("Bad score.")
except :
    print("Bad score.")
