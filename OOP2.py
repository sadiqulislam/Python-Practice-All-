
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