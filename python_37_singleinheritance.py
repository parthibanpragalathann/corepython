#Single Inheritance in Python


# Single Inheritance in Python
# In python single inheritance, a derived class is derived only from a single parent class and allows the class to derive behaviour and properties from a single base class.
# This enables code re usability of a parent class, and adding new features to a class makes code more readable, elegant and less redundant. And thus,
# single inheritance is much more safer than multiple inheritances if it's done in the right way and enables derived class to call parent class method and
# also to override parent classes existing methods.

# Source Code
class Nokia:
    company = "Nokia India"
    webiste = "www.nokia-india.com"

    def contact_details(self):
        print("Address : Cherry Road,Near Bus Stand ,Salem")


class Nokia1100(Nokia):
    def __init__(self):
        self.name = "Nokia 1100"
        self.year = 1998

    def product_details(self):
        print("Name     : ", self.name)
        print("Year     : ", self.year)
        print("Company  : ", self.company)
        print("Website  : ", self.webiste)


mobile = Nokia1100()
mobile.product_details()
mobile.contact_details()



