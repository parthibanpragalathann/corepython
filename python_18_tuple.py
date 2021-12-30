'''
TUPLE IN PYTHON
Tuple an immutable sequence of elements stored enclosing within the parenthesis.


'''

#Tuple create
tuple_var = tuple()     # tuple constructor

tuple_val=(1, 2, 3, "a", "b")
print("tuple values ", tuple_val)
print("tuple value type ", type(tuple_val))

t= (1, 11, 21, 31)
print("max value in  the tuple ", max(t))
print("min value in  the tuple ", min(t))
print("count value in  the tuple ", t.count(1))
print("split value in  the tuple ", t[1:3])
print("len value in  the tuple ", len(t))


for i, j in enumerate("abc"):
    print(i, j)


#output
'''
tuple values  (1, 2, 3, 'a', 'b')
tuple value type  <class 'tuple'>
max value in  the tuple  31
min value in  the tuple  1
count value in  the tuple  1
split value in  the tuple  (11, 21)
len value in  the tuple  4

0 a
1 b
2 c

'''



