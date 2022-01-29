#Static Method in Python

# Static methods, much like class methods, are methods that are bound to a class rather than its object.
# They do not require a class instance creation.
# So, they are not dependent on the state of the object.

# Source Code
# Static Method in Python

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printDetail(self):
        print("Name : ", self.name, "  Age : ", self.age)

    @staticmethod
    def welcome():
        print("Welcome to our Institution")


s1 = student("fidel castro", 25)
s1.printDetail()
s1.welcome()


s2 = student("Velupillai Prabhakaran", 45)
s2.printDetail()
s2.welcome()



