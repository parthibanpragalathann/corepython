#Abstract Base Class in Python

# An abstract class can be considered as a blueprint for other classes. It allows you to create a set of methods that must be created within any child classes built from the abstract class. A class which contains one or more abstract methods is called an abstract class. An abstract method is a method that has a declaration but does not have an implementation. While we are designing large functional units we use an abstract class. When we want to provide a common interface for different implementations of a component, we use an abstract class.

#Source Code
from abc import ABC, abstractmethod


class Bank(ABC):
    @abstractmethod
    def loan(self): pass

    @abstractmethod
    def credit(self): pass

    @abstractmethod
    def debit(self): pass

class HDFC(Bank):
    def loan(self):
        print("We can Provide 7.5% Interest Loan")

    def credit(self):
        print("HDFC Provide Credit")

    def debit(self):
        print("HDFC Provide Debit")

    def card(self):
        print("HDFC Provide Credit Card")
o=HDFC()
o.loan()
o.credit()
o.debit()
o.card()
