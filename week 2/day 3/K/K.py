part1 = input().split()
n = int(part1[0])
h = int(part1[1]) * 3

found = "NO"

for i in range(0, n):
    trainings = input().split()
    sum = 0
    for training in trainings:
        sum = sum + int(training)
    if sum >= h:
        found = "YES"
        break

print(found)

    
