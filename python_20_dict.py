'''

Dictionary in python

dictionary is mapping from a set of key to their corresponding values.

key-value pair the representation of the mapping key to a value.
items the another name for key value pair
key  that represent the dictionary first part of key-value pair
value is second part of key-value pair
hashtable is used to implement python dictionary.
memo a computer value stored to avoid unnecessary feature computation.
flag a boolean variable indicate whether a condition is  True


from keys - return to merge key values
get - return value of the specify key
items - return only from list of dict from dictionary
set default - if does not exited insert the key with a value in the dictionary
pop - remove random random key value
pop item - remove specified item from the dictionary.

'''

student = {
    'name': "agni",
    'age': 21
}
print(student)
print(type(student))
print(student.get('name'))
print(student.keys())
print(student.values())
print(student.items())
for i, j in student.items():
    print("using for loop ", i, j)

students=student.copy()

print(students)
# print(student.clear())
print(students.update({'gender': 'male'}))
print(students)
print(students.pop('gender'))
print(students)
print(students.popitem())
print(students)
print(students.clear())
students.setdefault('name', 'parthi')
print(students)

data = {
    'profile': "agni"
}

data_ = {
    'gender':'male',
    'image': "agni.jpg"
}


print(dict.fromkeys(data, data_))


'''
{'name': 'agni', 'age': 21}
<class 'dict'>
agni
dict_keys(['name', 'age'])
dict_values(['agni', 21])
dict_items([('name', 'agni'), ('age', 21)])
using for loop  name agni
using for loop  age 21
{'name': 'agni', 'age': 21}
None
{'name': 'agni', 'age': 21, 'gender': 'male'}
male
{'name': 'agni', 'age': 21}
('age', 21)
{'name': 'agni'}
None
{'name': 'parthi'}
{'profile': {'gender': 'male', 'image': 'agni.jpg'}}
'''
