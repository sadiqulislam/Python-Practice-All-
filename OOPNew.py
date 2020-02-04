class Student:
    def __init__(self, name, age, contact, dept):
        self.name = name
        self.age = age
        self.contact = contact
        self.dept = dept

    def getdata(self):
        print("Accepting Data!")
        self.name = input("Enter Your Name: ")
        self.age = input("Enter Your Age: ")
        self.contact = input("Enter Your Contact Number: ")
        self.dept = input("Enter Your Department: ")


    def display(self):
        print(f"Name Is {self.name} \n Age Is {self.age} \n Contact Is {self.contact} \n Department Is {self.dept}")

Shishir = Student("Blank" , "0", "0", "Nill")
Shishir.getdata()
Shishir.display()