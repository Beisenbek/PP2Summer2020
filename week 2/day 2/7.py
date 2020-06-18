n = int(input())

alive = True
while alive:
    d = n % 10
    print(d)
    n = n // 10
    alive = n > 0


