# Multiple Inheritance in Python

# When a class is derived from more than one base class it is called multiple Inheritance. The derived class inherits all the features of the base case.

# Source Code
# Multiple Inheritance

class Father:
    def fishing(self):
        print("Fishing in Rivers")

    def chess(self):
        print("Playing Chess From Father")


class Mother:
    def cooking(self):
        print("Cooking Food")

    def chess(self):
        print("Playing Chess From Mother")


class Son(Mother,Father):
    def ride(self):
        print("Riding Bicycle")
o = Son()
o.ride()
o.fishing()
o.cooking()
o.chess()

