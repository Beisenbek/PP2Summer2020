def numberOfDigits(n):
    res = 0
    while(True):
        res = res + 1
        n = n // 10
        if n == 0: break
    return res

def firstDigit(n, k):
    x = pow(10, k - 1)
    return n // x

n = int(input())
k = numberOfDigits(n)
res = True
leadingZero = False

for i in range(0, k // 2):
    a = numberOfDigits(n)
    expectedLength = a - 2
    r = n % 10
    n = n // 10
    l = 0

    if leadingZero == False:
        l = firstDigit(n, a - 1)
        n = n - l * pow(10, a - 2)
    else:
        leadingZero = False
        expectedLength = a - 1
    
    if l != r:
        res = False
        break

    actualLength = numberOfDigits(n)

    if actualLength != expectedLength:
        leadingZero = True
   

if res : print("YES")
else : print("NO")