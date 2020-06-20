def f(a, d, k, n):
    if k > n: return a
    return f(a + d, d, k + 1, n)


parts = input().split()
a = int(parts[0])
b = int(parts[1])

if b < 0: print(f(a, -1, 1, abs(b)))
else: print(f(a, 1, 1, abs(b)))

#print(f(a, (?????):1?-1, 1, abs(b)))
