class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def sqr(self):
        return  self.a * self.b
    def pr(self):
        return  2 * (self.a  +  self.b)


rec = Rectangle(20, 10)
print(rec.sqr())
print(rec.pr())

