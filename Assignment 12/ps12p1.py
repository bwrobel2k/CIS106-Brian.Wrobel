last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "White"]
c=0


def normal(last_names,c):
  while c <= 9:
    print(last_names[c])
    c=c+1
  

def reverse(last_names,c):
  c = len(last_names) - 1
  while c >= 0:
    print(last_names[c])
    c=c-1



normal(last_names,c)

reverse(last_names,c)