last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "White"]
exam_scores = [85, 92, 78, 90, 88, 76, 94, 82, 89, 91]
c=0


def normal(last_names,c):
  while c <= 9:
    print(last_names[c])
    print(exam_scores[c])
    c=c+1
  

def reverse(last_names,c):
  c = len(last_names) - 1
  while c >= 0:
    print(last_names[c])
    print(exam_scores[c])
    c=c-1



normal(last_names,c)

reverse(last_names,c)