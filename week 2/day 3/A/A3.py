x = int(input())
y = x
n = 0

while(y):
    n = n * 10 + (y % 10)
    y //= 10

if(n == x):
    print("YES")
else:
    print("NO")