a = input()
k = len(a)//2
print(k)
res = True

for i in range(0, k):
    if a[i] != a[-i-1]:
        res = False
        break

if res != True: print("NO")
else: print("YES")