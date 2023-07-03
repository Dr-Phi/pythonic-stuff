# open(input('Enter file name: '))

try:
  fhandle = open('mbox-short.txt')
except:
  print('Verify the filename')
  exit()

senders = list()
for line in fhandle:
  if line.startswith('From'):
    words = line.split()
    print(words[1])
    senders.append(words[1])

print(f'There were {len(senders)} lines with senders in the file')