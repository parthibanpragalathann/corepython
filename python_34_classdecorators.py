# The python decorators in class method() is an inbuilt function in Python, which returns a class method for a function.

# Source Code
class student:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        student.count += 1

    def printDetail(self):
        print("Name  : ", self.name, "  Age : ", self.age)

    @classmethod
    def total(cls):
        return cls.count


o = student("che guevara", 25)
o.printDetail()
a = student("Raja", 45)
a.printDetail()

print("Total Admission :", student.total())
print("Total Admission :", o.total())
