def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

s = input().split()
a = int(s[0])
b = int(s[1])

print(lcm(a, b) + gcd(a, b))