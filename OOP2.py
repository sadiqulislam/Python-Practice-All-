# One Object
class Restaurent():
    name = ""
    owner = ""

    def details(self):
        print(self.name)
        print(self.owner)

    def details_with_address(self,address):
        print(self.name)
        print(self.owner)
        print(address)

restaurent1 = Restaurent()
restaurent1.name="Star Kabab"
restaurent1.owner ="Shyam"
restaurent1.details()
restaurent1.details_with_address('Dhanmondi')


class Person():

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def details2(self):
        print(self.name,self.age,sep=',')

shishir = Person("Shishir",23)
print(shishir.details2())
shishir.details2()

#Multiple Object:

class Course():

    def __init__(self,name,code):
        self.c_name=name
        self.c_code=code

    def c_details(self):
        print(self.c_name,self.c_code,sep=',')

course_list =[]

for c in range(0,3):
    course=Course("Course " +str(c),311+c)
    course_list += [course]

for c in course_list:
    c.c_details()
