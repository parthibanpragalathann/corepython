#Operator Overloading in Python

# Operator Overloading means giving extended meaning beyond their predefined operational meaning. For example operator + is used to add two integers as well as join two strings and merge two lists. It is achievable because "+" operator is overloaded by int class and str class. You might have noticed that the same built-in operator or function shows different behaviour for objects of different classes, this is called Operator Overloading.

# Source Code
'''
a = 10
b = 20
print(a + b)

a = "pArthiban"
b = "Duce"
print(a + b)
'''

class Addition:
    def __init__(self, a):
        self.a = a

    def __add__(o1, o2):
        return o1.a + o2.a

    def __sub__(o1, o2):
        return o1.a - o2.a


o1 = Addition(10)
o2 = Addition(20)

print("Total      : ", (o1 + o2))
print("Difference : ", (o1 - o2))

'''
Operator    Magic Method
+   __add__(self, other)
-   __sub__(self, other)
*   __mul__(self, other)
/   __truediv__(self, other)
//  __floordiv__(self, other)
%   __mod__(self, other)
**  __pow__(self, other)
>>  __rshift__(self, other)
<<  __lshift__(self, other)
&   __and__(self, other)
|   __or__(self, other)
^   __xor__(self, other)

Comparison Operators :
Operator    Magic Method
<   __LT__(SELF, OTHER)
>   __GT__(SELF, OTHER)
<=  __LE__(SELF, OTHER)
>=  __GE__(SELF, OTHER)
==  __EQ__(SELF, OTHER)
!=  __NE__(SELF, OTHER)

Assignment Operators :
Operator    Magic Method
-=  __ISUB__(SELF, OTHER)
+=  __IADD__(SELF, OTHER)
*=  __IMUL__(SELF, OTHER)
/=  __IDIV__(SELF, OTHER)
//= __IFLOORDIV__(SELF, OTHER)
%=  __IMOD__(SELF, OTHER)
**= __IPOW__(SELF, OTHER)
>>= __IRSHIFT__(SELF, OTHER)
<<= __ILSHIFT__(SELF, OTHER)
&=  __IAND__(SELF, OTHER)
|=  __IOR__(SELF, OTHER)
^=  __IXOR__(SELF, OTHER)

Unary Operators :
Operator    Magic Method
-   __NEG__(SELF, OTHER)
+   __POS__(SELF, OTHER)
~   __INVERT__(SELF, OTHER)
'''


