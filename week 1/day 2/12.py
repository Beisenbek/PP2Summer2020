def f(a):
    return a + 10

x = lambda a : a + 10

print((lambda a : a + 10)(5))
print((lambda a : a + 10)(10))
print(f(5))
print(x(5))
print(x(51))