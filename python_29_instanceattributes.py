#Instance attributes
# A class is a blueprint for the creation of different objects. When the objects get created to form the class,
# they no longer depend on the class attribute.
# Also, the class has no control over the attributes of the instances created.

# Source Code
class user:
    course = 'Java'

o = user()
print(user.__dict__)
print(user.course)  # Print Class attribute
print(o.__dict__)
print(o.course)
o.course = "C++"
print(o.__dict__)
print(o.course)

o2 = user()
print(o2.course)
