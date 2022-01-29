# Multilevel Inheritance in Python

# In multilevel inheritance, features of the base class and the derived class are inherited into the new derived class.

# Source Code
class GrandFather:
    def ownHouse(self):
        print("Grandpa House")


class Father(GrandFather):
    def ownBike(self):
        print("Father's Bike")


class Son(Father):
    def ownBook(self):
        print("Son Have a Book")


o = Son()
o.ownHouse()
o.ownBike()
o.ownBook()
