#1..n
#s(n) = s(n-1) + n
#s(n-1) = s(n-2) + n - 1

#n = 100.......1 ... 0 , -1, -2, -3..

def rec(n):
  if n == 1: return 1
  return rec(n - 1) + n

print(rec(10))