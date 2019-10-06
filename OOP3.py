#In-Direct Modification

class Person():

    def __init__(self,name,age):
        self.name = name
        self.age= age

    def change_name(self,name):
        self.name= name

    def details(self):
        print(self.name,self.age)

person = Person("The Presence",23)

person.details()

person.change_name("Shishir")
person.details()

#Direct Modification:

class Course():
    def __init__(self,c_name,c_code):
        self.c_name = c_name
        self.c_code = c_code

    def c_details(self):
        print(self.c_name,self.c_code)

course = Course("Ethics","444")
course.c_name = "Robotics"
course.c_details()