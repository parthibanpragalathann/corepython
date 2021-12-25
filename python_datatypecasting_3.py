'''
Datatype type casting
define the type of data or A category of values

python data types

INT      - positive or negative whole number without decimal of unlimited length.
FLOAT    - floating point number one or more decimals
COMPLEX  - writen with j as the imaginary part
RANDOM   - random functions make a random number
STRING   - sequence of character
LIST     - sequence of different type values stored with in square brackets
TUPLES   - sequence of different type values stored with in parenthesis
DICT     - key value pair
SET      - unique data set python provides
frozenset- returns an unchangeable object (which is like a read only set & only unchangeable)
BooL     - True or False values

python provides type function it is used to identify the type of data. type()
'''
import random

int_data = 10
float_data = 10.10
str_data = "ten"
complex_data = 10+10j
random_data = random.randint(1, 10)
list_data = [1, "a", 1+3j, 10.0]
tuple_data = (1, "a", 1+3j, 10.0)
set_data = {1, "1", 1.1, 1}
frozenset_data = frozenset({1, 1, "a", "b"})
dict_data = {"a": 1, "b": 10}
bool_data = True

print("this data type ", type(int_data), "data is ", int_data, "\n")
print("this data type ", type(float_data), "data is ", float_data, "\n")
print("this data type ", type(str_data), "data is ", str_data, "\n")
print("this data type ", type(complex_data), "data is ", complex_data, "\n")
print("this data type ", type(random_data), "data is ", random_data, "\n")
print("this data type ", type(list_data), "data is ", list_data, "\n")
print("this data type ", type(tuple_data), "data is ", tuple_data, "\n")
print("this data type ", type(set_data), "data is ", set_data, "\n")
print("this data type ", type(frozenset_data), "data is ", frozenset_data, "\n")
print("this data type ", type(dict_data), "data is ", dict_data, "\n")
print("this data type ", type(bool_data), "data is ", bool_data, "\n")

#Type casting
'''
data convert into one data type to another data type
'''
int_str_data = str(int_data)
folat_int_data = int(float_data)
str_list_data = list(str_data)

print(int_data, "this int data convert into string ", int_str_data)
print(float_data, "this float data convert into int ", folat_int_data)
print(str_data, "this string data convert into list ", str_list_data)


'''output

this data type  <class 'int'> data is  10 

this data type  <class 'float'> data is  10.1 

this data type  <class 'str'> data is  ten 

this data type  <class 'complex'> data is  (10+10j) 

this data type  <class 'int'> data is  1 

this data type  <class 'list'> data is  [1, 'a', (1+3j), 10.0] 

this data type  <class 'tuple'> data is  (1, 'a', (1+3j), 10.0) 

this data type  <class 'set'> data is  {1, '1', 1.1} 

this data type  <class 'frozenset'> data is  frozenset({1, 'a', 'b'}) 

this data type  <class 'dict'> data is  {'a': 1, 'b': 10} 

this data type  <class 'bool'> data is  True 

10 this int data convert into string  10
10.1 this float data convert into int  10
ten this string data convert into list  ['t', 'e', 'n']

'''