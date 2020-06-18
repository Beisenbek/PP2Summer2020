class MyClass:
    def __init__(self, x):
        self.x = x  
    x = 5

p1 = MyClass(10)
p2 = MyClass(20)

print(p1.x)
print(p2.x)

print(MyClass.x)