'''
Identity Operator in python
It's used to if value or not and equal or not in the given variable
is values are in the variable
isnot values are not in the variable
'''
a=['a', 'b', 'c']
b=['a', 'b', 'c']
c=a
print("identity of the variable a ", id(a))
print("identity of the variable b ", id(b))
print("identity of the variable c ", id(c))

print("using IS ", a is b)
print("using IS ", a is c)
print("using IS NOT ", a is not b)
print("using IS NOT ", a is not c)
print("Equal ", a==b)
print("NOt Equal ", a!=b)

'''
OUTPUT

identity of the variable a  1898391034752
identity of the variable b  1898391032320
identity of the variable c  1898391034752
using IS  False
using IS  True
using IS NOT  True
using IS NOT  False
Equal  True
NOt Equal  False
'''
