#Function Overriding in Python

# It is used to change the behavior of existing methods and there is a need for at least two classes for method overriding generally used term for an ambiguity that arises when two classes B and C inherit from a superclass A, and another class D inherits from both B and C.

# Source Code
class A:
    def display(self):
        print("I am the display of Class A")


class B(A):
    def display(self):
        print("I am the display of Class B")

class C(A):
    pass
    # def display(self):
    #     print("I am the display of Class C")

class D(C):
    pass
    # def display(self):
    #     print("I am the display of Class D")


o = D()
o.display()
