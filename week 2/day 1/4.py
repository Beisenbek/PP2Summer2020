f = open("files/demofile.txt","r")#relative path
print(f.read())
f.close()

f1 = open("../test3.txt","r")#relative path
print(f1.read())
f1.close()

f2 = open("/Users/bsnbk/Desktop/test.txt","r")#absolute path
print(f2.read())
f2.close()