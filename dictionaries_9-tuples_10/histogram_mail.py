import pprint
fhandle = open('mbox-short.txt')

msg_per_user = {}

for line in fhandle:
  if line.startswith("From"):
    words = line.split()
    msg_per_user.setdefault(words[1], 0)
    msg_per_user[words[1]] += 1

pprint.pprint(msg_per_user)

bigcount = None
bigword = None
for word, times in msg_per_user.items():
  if bigcount is None or times > bigcount:
    bigword = word
    bigcount = times

print("The most frequent sender is: ", bigword,"\n", "Emails sent: ", bigcount)