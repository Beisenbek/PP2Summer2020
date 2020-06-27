def f(c, n):
    i = ord(c) - 65
    if n < 0: return chr((i - abs(n) % 26 + 26) % 26 + 65)
    return chr((i + n) % 26 + 65)

n = int(input())
s = input()
r = ""
for x in s:
    r += f(x, n)

print(r)