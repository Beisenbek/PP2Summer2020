def myfunc(n):
  return lambda a : a * n

x = myfunc(10)


print(x(2))
print(x(3))