f = open("data", "r")
battingavg = f.readline()
lastn = []
avg = []
c=0
while battingavg != "":
  c = c + 1
  lastn.append(str(battingavg).rstrip("\n"))
  avg.append(float(f.readline()))
  battingavg = f.readline()

def display(lastn, avg):
  print(lastn)
  print(avg)
  
def search(lastname, lastn, avg):
  c=0
  index = 0
  while c < len(lastn):
    if lastn[c] == lastname:
      index = c
      c += 1
    else:
      c += 1
  print("Lastname: ", lastn[index])
  print("Batting Average: ", avg[index])
display(lastn, avg)
cont = "y"

while cont == "y":
  
  lastname = input("What is the last name?")
  index = search(lastname,lastn,avg)
 
  
