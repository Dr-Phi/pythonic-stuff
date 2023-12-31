import string
filen = input("filename: ")
fhand = open(filen, encoding="utf-8")
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

fout = open('output.txt', 'w', encoding='utf-8')

for key, val in lst[350:390]:
    fout.write(val)
    print(value, key)
    