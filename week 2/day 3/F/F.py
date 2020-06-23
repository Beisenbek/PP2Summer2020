memory = list(list())

def f(a,b):
    if a == 1 or b == 1: return 1
    if memory[a][b] != -1: return memory[a][b]
    memory[a][b] = f(a-1,b) + f(a,b-1)
    return memory[a][b]

a,b =map(int, input().split())

for i in range(0, a + 1):
    row = []
    for j in range(0, b + 1):
        row.append(-1)
    memory.append(row)

print(f(a,b))