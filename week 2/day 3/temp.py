s = input()
x = 0
y = 0
for i in range(0 , len(s)):
    if(s[i] == 'U'):
        y = y + 1
    elif(s[i] == 'D'):
        y = y - 1
    elif(s[i] == 'R'):
        x = x + 1
    elif(s[i] == 'L'):
        x = x - 1
    
    if x == 0 and  y == 0:
       print("True")
    else:
        print("False")
