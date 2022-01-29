#A decorator feature in Python wraps in a function, appends several functionalities to existing code and then returns it.
# Methods and functions are known to be callable as they can be called. Therefore, a decorator is also a callable that returns callable.
# This is also known as meta programming as at compile time a section of program alters another section of the program.
#programmers modifying the behaviour of functions or class, add new functionalities to an existing object without modifying it's structure.

#Source Code
# Property Decorator
class user:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.msg = self.name + " is " + str(self.age) + " years old"

    @property
    def msg(self):
        return self.name + " is " + str(self.age) + " years old"


o = user("PArthiban", 25)
print(o.name)
print(o.age)
print(o.msg)
o.age = 45
print(o.msg)
