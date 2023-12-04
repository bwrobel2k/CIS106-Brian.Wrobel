lname = input("Enter bowler's last name: ")
game1 = float(input("Enter game 1 score: "))
game2 = float(input("Enter game 2 score: "))
game3 = float(input("Enter game 3 score: "))
handicap = float(input("Enter handicap: "))

def process(game1, game2, game3, handicap):
  average = (game1 + game2 + game3) / 3
  averagehandicap = (game1 + game2 + game3 + handicap) / 3
  return average, averagehandicap

average, averagehandicap = process(game1, game2, game3, handicap)

print("Bowler's last name: ", lname)
print("Average score: ", average)
print("Average score with handicap: ", averagehandicap)