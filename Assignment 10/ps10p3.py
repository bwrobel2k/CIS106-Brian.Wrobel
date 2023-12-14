continuee = str(input("Would you like to continue the program? (y/n)"))
MSRPtotal=0
alltotal=0
def outthedoor(MSRP,make,model,electricvehiclecode):
  global MSRPtotal
  global alltotal

  
  if make == "Honda" and model == "Accord":
    discount = .1
  elif make == "Toyota" and model == "Rav4":
    discount = .15
  elif electricvehiclecode == "y":
    discount = .3
  else:
    discount = .05

  total = (MSRP - (MSRP * discount)) + (MSRP * .07)
  MSRPtotal = MSRPtotal + MSRP
  alltotal = alltotal + total
  return (total, MSRPtotal, alltotal)




while continuee == "y":
  make = str(input("What is the make of the vehicle?"))
  model = str(input("What is the model of the vehicle?"))
  electricvehiclecode = str(input("Is the vehicle electric? (y/n)"))
  MSRP = float(input("What is the MSRP of the vehicle?"))
  total = outthedoor(MSRP,make,model,electricvehiclecode)
  print("The price out the door ",total[0])
  continuee = str(input("Would you like to continue the program? (y/n)"))


print("The sum of all MSRP's",total[1])
print("The sum of all final totals",total[2])
  