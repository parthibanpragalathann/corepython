# In Python, getters and setters are not the same as those in other object-oriented programming languages.
# Basically, the main purpose of using getters and setters in object-oriented programs is to ensure data encapsulation.
# Private variables in python are not actually hidden fields like in other object oriented languages.

# Source Code
class student:
    def __init__(self, total):
        self._total = total

    def average(self):
        return self._total / 5.0

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, t):
        if t < 0 or t > 500:
            print("Invalid Total and can't Change")
        else:
            self._total = t


o = student(450)
print("Total   : ", o.total)
print("Average : ", o.average())
o.total = 550
print("Total   : ", o.total)
print("Average : ", o.average())
