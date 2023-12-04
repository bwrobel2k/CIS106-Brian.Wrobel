lname = input("Enter the salesperson's last name: ")
sales = float(input("Enter the amount of sales: "))

def process(sales):
  if sales > 100000.00:
    commission = sales * 0.10
  else:
    commission = sales * 0.05

  nextyearstarget = sales * 0.05
  return commission,nextyearstarget

commission,nextyearstarget = process(sales)


print("Salesperson's last name: ",lname)
print("Commission:             $",commission)
print("Next years target:      $",nextyearstarget)