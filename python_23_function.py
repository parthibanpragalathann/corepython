'''
FUNCTIONS IN PYTHON

Why Function?
function can make a program to eliminate repetitive code. and reuse it.

functions are FRUITFUL AND VOID
perform an action with return value that's called fruitful function
perform an action but not return value that's called void function
using def keyword to define the function structure  with provide the function name and  open close parenthesis semi colan
then write a what we want to perform for computation.
arguments are passed real value to the functions.
parameters are initialized to the values of the arguments supplied.
module is a file contains a collection of related function and other definition
dot notation the syntax for calling function an another module. (.)
'''

#No return value without argument
def print_lyrics():
    print("Pain! You made me a, you made me a believer, believer")

print_lyrics()

'''
output
Pain! You made me a, you made me a believer, believer
'''

#No return value with argument

def print_dialog(dialog):
    print(dialog)

print_dialog("beliver always belive himself")

'''
OUTPUT
beliver always belive himself
'''

#return value with parameter(intialized value pass function to perform action)
def param(name, city="Trichy"):
    return name, city

print(param("parthiban"))
'''
OUTPUT
('parthiban', 'Trichy')
'''

#return with arbitrary argument (*)
def arbitary(*data):
    return data

x=arbitary("parthiban", 21, "python developer")
print(x)

'''
OUTPUT
('parthiban', 21, 'python developer')

'''
#return keyword argument
def student(name, age):
    return name, age

y=student(age=22, name="parthiban")
print(y)
'''
OUTPUT
('parthiban', 22)
'''


#return keyword arbitrary argument
def keyword_arbitrary(**data):
    return(data)

s=keyword_arbitrary(name="parthiban", age=22, city="omandur")
print(s)

'''
OUTPUT
{'name': 'parthiban', 'age': 22, 'city': 'omandur'}
'''

#list as argument
def total(total_list):
    return sum(total_list)

q=total([10, 10, 10])
print(q)
'''
output
30
'''

#Recursive function
#1*2*3=6
def factorial(n):
    if n==1:
        return 1
    else:
        return (n * factorial(n-1))

w=factorial(3)
print("factorial", w)

'''
OUTPUT
factorial 6
'''

#lambda function simple syntax for function(anonymous function)
#z is function name a is argument for (a+50)action to perform in the function
z = lambda a:a+50
y=z(50)
print("lambda function ", y)
'''
OUTPUT
lambda function  100
'''
