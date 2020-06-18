n = int(input())

'''
n = 123
1
2
3
'''
d = n % 10
print(d)
n = n // 10

while n > 0:
    d = n % 10
    print(d)
    n = n // 10


