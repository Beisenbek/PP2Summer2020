class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  x =  12 

  def myfunc(self):
    print("Hello my name is " + self.name + " " + str(Person.x))

p1 = Person("John", 36)
p1.myfunc()


p2 = Person("Smith", 20)
p2.myfunc()
