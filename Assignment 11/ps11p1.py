qty = int(input("The amount of the item: "))
price = int(input("The price of the item: "))
discountrate = float(input("What is the discount amount: "))

def process(qty, price, discountrate):
  extprice = qty * price
  discountamt = extprice * discountrate
  discountprice = extprice - discountamt
  return discountprice, discountamt


discountprice, discountamt = process(qty,price,discountrate)

print("The amount of items you purchased",qty)
print("The price per item is           $",price)
print("The amount of money saved       $", discountamt,)
print("The discounted price $          $", discountprice)