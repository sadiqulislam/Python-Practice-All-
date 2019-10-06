#LifeCycle Of An Object:

class Person():
    def __init__(self,name):
        self.name=name
        print(self.name + " Created")

    def __del__(self):
        print(self.name + " Deleted")

person1 = Person("Shishir")