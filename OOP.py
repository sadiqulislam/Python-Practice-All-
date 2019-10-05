# Object Oriented Programming:

class  Student:

    __name = None        # Private Variable
    __id = 0
    __section = None


    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

shishir = Student()
shishir.set_name("Shishir")
ob1 = shishir.get_name()
print(ob1)



# Object oriented programming
'''

class Employee:
    __name = None
    __id = 0
    __salary = 0

    def __init__(self, name, id, salary):
        self.__name = name
        self.__id = id
        self.__salary = salary

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_salary(self, salary):
        self.__id = salary

    def get_salary(self):
        return self.__salary

harry = Employee('harry', 420, 70000000)

print(harry.get_salary())

'''
