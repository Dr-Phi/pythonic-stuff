'''This program counts the distribution of the hour of the day for each
of the messages. For each hour, print out the counts.

04 means 4 am 
15 means 3 pm ...
'''

import pprint
fhandle = open('mbox-short.txt')

hours_sent = {}

for line in fhandle:
  if line.startswith("From"):
    # print(line)
    words = line.split(":")
    if len(words) < 3: continue
    hours_sent.setdefault(words[0][-2:], 0)
    hours_sent[words[0][-2:]] += 1

pprint.pprint(hours_sent)