class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Bob")
p2 = Person("Bob")

print(p1 is p2)