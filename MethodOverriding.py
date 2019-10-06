#Method Overriding And Call Class From Method:

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def details(self):
        return str(self.name) + " " + str(self.age)

class Address(Person):
    def __init__(self,name,age):
        super().__init__(name,age)

    def details(self):                                        #Overriding
        return str(self.name) + " " + str(self.age) + " " + "Dhaka"

    def full_details(self):
        print("Details Of Parent Class Without Address",super().details())     # Call From Method
        print("Details Of Child Class With Address",self.details())


person = Address("Shishir",23)
person.full_details()