continuee = str(input("Would you like to continue the program? (y/n)"))
paintrequired = 0

def squarefootage(roomlength,roomheight,roomwidth):
  squarefeet = (2 * roomlength * roomwidth) + (2 * roomlength * roomheight) +\
  (2 * roomwidth * roomheight)
  paintrequired = squarefeet / 50
  return paintrequired
  

while continuee == "y":
  roomlength = float(input("What is the length of the room?"))
  roomheight = float(input("What is the height of the room?"))
  roomwidth = float(input("What is the width of the room?"))
  paintrequired = squarefootage(roomlength,roomheight,roomwidth)
  print("The amount of gallons of paint required is: ",paintrequired)
  continuee = str(input("Would you like to continue the program? (y/n)"))
  
  