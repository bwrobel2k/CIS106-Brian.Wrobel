continuee = str(input("Would you like to continue the program? (y/n)"))
totalticketprice = 0

def trainticket(milesfromdowntown):
  if milesfromdowntown >= 30:
    trainticketprice = 12
  elif milesfromdowntown >= 20:
    trainticketprice = 10
  elif milesfromdowntown >= 10:
    trainticketprice = 8
  else:
    trainticketprice = 5
    
  return trainticketprice
  
  


while continuee == "y":
  lname = str(input("Please enter your last name: "))
  milesfromdowntown = int(input("Please enter the miles from downtown: "))
  trainticketprice = trainticket(milesfromdowntown)
  print("The train ticket price is: $",trainticketprice)
  totalticketprice = totalticketprice + trainticketprice
  continuee = str(input("Would you like to continue the program? (y/n)"))

print("Your total for all tickets is: $", totalticketprice)
  