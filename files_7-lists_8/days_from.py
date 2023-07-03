fhandle = open('mbox-short.txt')

for line in fhandle:
  if line.startswith('From'):
    day = line.split()
    if len(day) < 3:
      continue
    print(day[2])
