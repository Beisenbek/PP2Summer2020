def f(x):
    if x == 1: return 1

    cnt = 0
    for i in range(2, x):
        if x % i == 0: cnt = cnt + 1

    return cnt + 2

n = int(input())

'''
n = 5
5 - 2
4 - 3
3 - 2
2 - 2
1 - 1
'''
while n > 0:
    c = f(n)
    print("{1} - {0}".format(n, c))
    n = n - 1

