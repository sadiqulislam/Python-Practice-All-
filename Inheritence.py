class Student:

    def __init__(self,name,age,contact,dept):

        self.name = name
        self.age = age
        self.contact = contact
        self.dept = dept

    def getdata(self):

        self.name = input("Name:")
        self.age = input("Age:")
        self.dept = input("Department: ")
        self.contact = input("Contact: ")

    def display(self):

        print(self.name,self.age,self.contact,self.dept,self.section)

class Cse(Student):

    def __init__(self,section):

        self.section = section

    def get(self):

        print("Accpting Inheritence Class Data")

        self.section = input("Section: ")

    def dis(self):

        print(self.section)

Shishir = Cse("Nill")
Shishir.get()
Shishir.getdata()
Shishir.display()