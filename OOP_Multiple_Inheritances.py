#Multiple Inheritances:

class Calculator():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def add(self):
        return self.x + self.y + self.z

class Math1 (Calculator):
    def __init__(self,x,y,z):
        super().__init__(x,y,z)

    def subtract(self):
        return self.x - self.y - self.z

class Math2 (Math1):
    def __init__(self,x,y,z):
        super(). __init__(x,y,z)

    def multiple(self):
        return self.x * self.y * self.z

class Math3():
    def division(self,x,y,z):
        return x / y /z


class Math4(Math2,Math3):
    def __init__(self,x,y,z):
        super(). __init__(x,y,z)

calculator = Math4(10,5,2)
print(calculator.multiple())
print(calculator.add())
print(calculator.division(x=calculator.x,y= calculator.y,z=calculator.z))
print(calculator.subtract())


