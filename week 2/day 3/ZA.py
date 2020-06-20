def filter2(s):
    if len(s) == 0: return False
    res = True
    for c in s:
        k = ord(c)
        if k < 97 or k > 122:
            res = False
            break
    return res

def filter1(s, t):
    res = 0
    for c in s:
        if c == t: res = res + 1
    return res == 1

def filter3(s):
    pos1 = s.find('@')
    pos2 = s.find('.')
    return pos1 < pos2

def solution(s):
    res = "No"
    if filter1(s, '@') and filter1(s, '.') and filter3(s):
        parts = s.split('@')
        aaa = parts[0]
        part2 = parts[1].split('.')
        bbb = part2[0]
        ccc = part2[1]
        if filter2(aaa) and filter2(bbb) and filter2(ccc):
            res = "Yes"
    return res

print(solution(input()))



