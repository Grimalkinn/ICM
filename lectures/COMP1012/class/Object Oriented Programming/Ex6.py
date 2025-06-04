from math import sqrt

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def mul(self):
        return self.a*self.b
    def sq(self):
        return sqrt(self.a)

p1=Math(4,5)

print(p1.add())
print(p1.mul())
print(p1.sq())