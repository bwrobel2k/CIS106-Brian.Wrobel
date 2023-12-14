continuee = str(input("Would you like to continue the program? (y/n)"))


def forcast(month,sales):
  if month == "Jan" or "Feb" or "Mar":
    forcastpercent = .1
  elif month == "Apr" or "May" or "Jun":
    forcastpercent = .15
  elif month == "Jul" or "Aug" or "Sep":
    forcastpercent = .2
  elif month == "Oct" or "Nov" or "Dec":
    forcastpercent = .25
  else:
    print("Invalid month")
  sales = sales * (1+forcastpercent)
  return sales

while continuee == "y":
  lname = str(input("What is your last name?"))
  month = str(input("What is the current month?"))
  sales = float(input("How much money earned in sales?"))
  sales = forcast(month,sales)
  print("Next months sales are expected to be: $", sales)
  continuee = str(input("Would you like to continue the program? (y/n)"))
  