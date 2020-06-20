f = open("input.txt", "r")
line = ""
for x in f:
  line = line + " " + x.strip()

parts = line.strip().split()

s = 0
for i in parts:
    s = s + int(i)


print(s)