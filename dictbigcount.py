name= input('Enter File Name:')
handle = open(name)
counts = dict()
bigcount = None
bigword = None
words = list()
for line in handle:
    if not line.startswith("From:") : continue
    line = line.split()
    words.append(line[1])
for word in words:
           counts[word] = counts.get(word, 0) + 1 
for key,val in counts.items() :
  if val > bigcount:
      bigcount = val
      bigword = key   
print(bigword,bigcount)
