#Inheritance :

class Math():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def sum(self):
        return self.x + self.y
    def multiple(self):
        return self.x * self.y

class MathExtend (Math):
    def __init__(self,x,y):
        super().__init__(x,y)

    def subtract(self):
        return self.x - self.y

math = MathExtend(10,5)
print("Addition Is",math.sum())
print("Subtract Is " ,math.subtract())
print("Multiplication Is ",math.multiple())