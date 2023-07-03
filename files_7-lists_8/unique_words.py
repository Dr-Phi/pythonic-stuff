try:
  fhandle = open(input('Enter file: '))
except:
  print('Make sure its a file')
  exit()

'''For each word, check to see if the word is already in a list. If the word is not in the list, add it to the list.'''
words = list()
for line in fhandle:
  lwords = line.split()
  for word in lwords:
    if word in words: continue
    else:
      words.append(word)
words.sort()

print(words)
