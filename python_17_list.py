'''

LIST IN PYTHON
List is a one of the build in data type in python
list is used to stored different type of sequence data with in square bracket.
list are mutable like modify easily and efficiently.
list is a not a fixed length.

list -  is a sequence of values
element - one of the value in a list
index - an integer value indicates an element in a list
list traversal - the sequential accessing of each element in a list
map - traverse a sequence and perform an operation on each element
object - something a variable can refer to, an object as type & value.
delimiter - when a string should be split

'''

#List is a sequence why?
list_seq = [1, 'a', 0.1, 3+10j]
print("different type of sequence data : ", list_seq)
print("1 type in the list : ", type(list_seq[0]))
print("a type in the list : ", type(list_seq[1]))
print("0.1 type in the list : ", type(list_seq[2]))
print("3+10j type in the list : ", type(list_seq[3]))
'''
Output
different type of sequence data :  [1, 'a', 0.1, (3+10j)]
Types stored data:
1 type in the list :  <class 'int'>
a type in the list :  <class 'str'>
0.1 type in the list :  <class 'float'>
3+10j type in the list :  <class 'complex'>

'''

#list are mutable
list_seq[0]= "mutable"
print("list are mutable : ", list_seq)

'''
output
list are mutable :  ['mutable', 'a', 0.1, (3+10j)]
'''

#Traversing a list
print("Traversing a list")
for i in list_seq:
    print(i)

'''
Traversing a list
mutable
a
0.1
(3+10j)
'''

#list operation

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print("sum of list :\n", list_a+list_b)
print("multiplication of list : \n", list_a*2)

#slice list
slice_list = ['a', 'b', 'c', 'd', 'e', 'f']
print("before slice the list : ", slice_list)
print("Display first element in the list using index : ", slice_list[0])
print("Display first element to fourth element in the list using index : ", slice_list[0:5])
print("Display last element in the list using negative index : ", slice_list[-1])
print("Display reverse all element in the list using negative index : ", slice_list[::-1])
print("Display first element to last second element in the list using positive & negative index : ", slice_list[1:-1])  # n-1

'''
output
before slice the list :  ['a', 'b', 'c', 'd', 'e', 'f']
Display first element in the list using index :  a
Display first element to fourth element in the list using index :  ['a', 'b', 'c', 'd', 'e']
Display last element in the list using negative index :  f
Display reverse all element in the list using negative index :  ['f', 'e', 'd', 'c', 'b', 'a']
Display first element to last second element in the list using positive & negative index :  ['b', 'c', 'd', 'e']
'''

#List methods
'''APPEND, EXTEND, COPY, COUNT, CLEAR, POP, REMOVE, REVERSE, SORT, INSERT'''

list_methods = []
print("Display the empty : ", list_methods)

#Append
print("Display add element in the  empty list  : ", list_methods.append("add"))
print("Display added element in the list : ", list_methods)


'''
Display the empty :  []
Display add element in the  empty list  :  None
Display added element in the list :  ['add']
'''

#Extend
extend_list = [1, 2, 3]
list_str = ['a', 'b', 'c']
extend_list.extend(list_str)
print("Two or more element or list add in the list such as extended :\n", extend_list)
'''
output
Two or more element or list add in the list such as extended :
 [1, 2, 3, 'a', 'b', 'c']
'''

#list copy
list_=[1, "a"]
b=list_.copy()
print("Copy the list in to b list ", b)
'''
output
Copy the list in to b list  [1, 'a']
'''

#list clear
list_val = [1, 2, 3]
print("list of values ", list_val)
print("Clear all the element in the list ", list_val.clear())

'''
output
list of values  [1, 2, 3]
Clear all the element in the list  None
'''

#List cout
count_list = ['a', 'z', 'b', 'z', 'c']
print("the length of the count list", len(count_list))
print("count of the element z in the list ", count_list.count('z'))

'''
output
the length of the count list 5
count of the element z in the list  2
'''

#List pop(remove element based on index)
pop_list=["q", "w", "e", "r"]
print("before using pop method in the list ", pop_list)
pop_list.pop(0)
print("remove 0th index element using pop method in the list ", pop_list)

'''
output
before using pop method in the list  ['q', 'w', 'e', 'r']
remove 0th index element using pop method in the list  ['w', 'e', 'r']
'''

#List remove (remove element based on element)
remove_list=['k', 'l', 'a', 's', 'd', 'f']
print("before using remove method in the list ", remove_list)
remove_list.remove('d')
print("using remove element d in the list \n", remove_list)

'''
output
before using remove method in the list  ['k', 'l', 'a', 's', 'd', 'f']
using remove method in the list 
 ['k', 'l', 'a', 's', 'f']
'''

#List Index
list_index=[23, 33, 43, 53]
print("Put the value to get value index ", list_index.index(43))

'''
output
Put the value to get value index  2
'''

#List Reverse
list_index.reverse()
print("Reverse the given list ", list_index)

'''
output
Reverse the given list  [53, 43, 33, 23]
'''

#List sort
list_index.sort()
print("sort the given list ", list_index)
'''
output
sort the given list  [23, 33, 43, 53]
'''
#List sort with reverse argument
list_index.sort(reverse=True)
print("sort with reverse argument using in the list", list_index)
'''
output
sort with reverse argument using in the list [53, 43, 33, 23]
'''

#List Insert pass the argument index and value
list_index.insert(1, 63)
print("insert element in the list", list_index)
"""
output
insert element in the list [53, 63, 43, 33, 23]
"""



#List sort using argument key len to display string element based on the length in the list
list_string=['zzzz', 'yy', 'xxx']
list_string.sort(key=len)
print(list_string)
'''
output
['yy', 'xxx', 'zzzz']
'''