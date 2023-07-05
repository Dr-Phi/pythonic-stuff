import pprint
fhandle = open('mbox.txt')

domains = {}

for line in fhandle:
  if line.startswith("From"):
    words = line.split()
    mail = words[1]
    domain = mail.split('@')[1]
    domains.setdefault(domain, 0)
    domains[domain] += 1

pprint.pprint(domains)

