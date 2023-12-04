qty = int(input("What is the quantity? "))
unitprice = float(input("What is the unit price? "))

tax = 0
total = 0
def process(qty, unitprice):
  global total, tax
  extprice = qty * unitprice
  tax = extprice * 0.07
  total = extprice + tax
  return total, tax

total, tax = process(qty, unitprice)
print("The total is $", total)
print("The tax is $", tax)