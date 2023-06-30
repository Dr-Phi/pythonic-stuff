def computegrade(score):
  if score > 1:
    print("Bad Score, enter number between 0.0 and 1")
  elif score <= 0.6:
    print("F")
  elif score < 0.7:
    print("D")
  elif score < 0.8:
    print("C")
  elif score < 0.9:
    print("B")
  else:
    print("A")

try:
  score = float(input("Enter score: "))
  computegrade(score)
except:
  print("Bad Score, enter number between 0.0 and 1")
