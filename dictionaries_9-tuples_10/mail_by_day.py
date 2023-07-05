try:
  fhandle = open(input('Ente file name: '))
except:
  print("Make sure it's the right file.")

days = {}

for line in fhandle:
  if line.startswith("From"):
    words = line.split()
    if len(words) < 3:continue
    else:
      days.setdefault(words[2], 0)
      days[words[2]] += 1

print(days) 