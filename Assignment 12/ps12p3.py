f = open("lastnames", "r")
lastname = f.readline()
lastn = []
score = []
c=0
highvar = 0
lowvar = 999
highindex= 0
lowindex = 0

while lastname != "":
  c = c + 1
  lastn.append(str(lastname).rstrip("\n"))
  score.append(int(f.readline()))
  lastname = f.readline()

def highandlow(score, highvar,lowvar,highindex,lowindex):
  highvar = score[0]
  lowvar = score[0]
  c=0
  while c < len(score):
    if score[c] > highvar:
      highvar = score[c]
      highindex=c
    elif score[c] < lowvar:
      lowvar = score[c]
      lowindex = c
    c=c+1  
  return highvar, lowvar, highindex, lowindex



highvar, lowvar, highindex, lowindex = highandlow(score, highvar,lowvar,highindex,lowindex)


print("Highest score: ", lastn[highindex], highvar)
print("Lowest score: ", lastn[lowindex], lowvar)