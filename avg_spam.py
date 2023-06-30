fname = input("Enter the file name: ")
fhand = open(fname)

values = []

for line in fhand:
  if line.startswith('X-DSPAM-Confidence:'):
    values.append(float(line[19:]))

sum = 0
for elem in values:
  sum += elem

print('Average spam confidence: ', sum / len(values))
