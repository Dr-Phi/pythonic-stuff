fname = input("Enter the file name: ")
if fname == 'na na boo boo':
  print("NA NA BOO BOO TO YOU - You have been punk'd")
  exit()
try:
  hfile = open(fname)
except:
  print('File cannot be opened: ', fname)
  exit()
count = 0
for line in hfile:
  count += 1
print(f'There were {count} subject lines in mbox.txt')