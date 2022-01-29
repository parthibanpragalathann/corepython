# INIT method
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created.
# Source Code
# init method in Python

class user:
    def __init__(self, name):
        print("Call When new Instance Created")
        self.name = name

    def printall(self):
        print("Name : ", self.name)
o1 = user("PARTHIba")

o1.printall()
print(o1.__dict__)
o2 = user("Duce")
o2.printall()
print(o2.__dict__)
print(user.__dict__)
