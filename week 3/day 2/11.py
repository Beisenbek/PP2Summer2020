f = open("input.txt", "r")

mylist = []
d = {}
for x in f:
  mylist.append(x.strip())
  d[x.strip()] = d.get(x.strip(), 0 ) + 1

mylist = list(dict.fromkeys(mylist))
mylist.sort()

for l in mylist:
  if int(d[l]) % 2 == 0: print(l)

