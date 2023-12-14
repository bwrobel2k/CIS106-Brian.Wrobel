continuee = str(input("Would you like to continue the program? (y/n)"))
totalsofmarketvalue = 0
totalassessedvalue = 0

def process(county,marketvalue):
  if county == "Cook":
    valuepercent = .9
  elif county == "Dupage":
    valuepercent = .8
  elif county == " McHenry":
    valuepercent = .75
  elif county == "Kane":
    valuepercent = .6
  else:
    valuepercent = .7

  assessedvalue = marketvalue * valuepercent
  return assessedvalue



while continuee == "y":
  county = str(input("What county is the property in?"))
  marketvalue = int(input("What is the market value of the property?"))
  assessedvalue = process(county,marketvalue)
  print("The assessed value of the property is: $",assessedvalue)
  totalsofmarketvalue = totalsofmarketvalue + marketvalue
  totalassessedvalue = totalassessedvalue + assessedvalue
  continuee = str(input("Would you like to continue the program? (y/n)"))

print("The total market value of all properties is: $",totalsofmarketvalue)
print("The total assessed value of all properties is: $",totalassessedvalue)