'''
read through a file and print the contents of the
file (line by line) all in upper case.
'''

fname = input("Enter a file name: ")
fhand = open(fname)

count = 0
for line in fhand:
  count += 1
  print(line.upper(), end='')

  if count == 17:
    exit()

