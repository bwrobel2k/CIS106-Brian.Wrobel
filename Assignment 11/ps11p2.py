lname = str(input("Enter your last name: "))
exam1 = int(input("Enter your first exam score: "))
exam2 = int(input("Enter your second exam score: "))
exam3 = int(input("Enter your third exam score: "))

def process(exam1, exam2, exam3):
  totalpoints = exam1+exam2+exam3
  avg = totalpoints/3
  return totalpoints,avg


totalpoints, avg = process(exam1, exam2, exam3)

print("Last name:          ", lname)
print("Total points:       ", totalpoints)
print("Average exam score: ", avg)