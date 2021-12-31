'''
SET IN PYTHON
SETS are unique elements order/index not necessary. enclosing within curly braces{}.duplicates not allowed.
SET methods {add, update, pop, remove, discard, clear, union, update, intersection, intersection_update, difference,
symmetric_difference, symmetric_difference_update, isdisjoint, issubset, issuperset}

add - used to add element in the set
update - value modify in the set
remove - value removed from the set not exist raise exception
discard - value removed from the set not exist not raise exception
pop - last element remove from the set
clear - remove all set value in the set
union - union of both set
intersection - same value of both set
intersection_update - intersection to update the set
difference - difference between both set
symmetric_difference - not same value from the
symmetric_difference_update - updated not same vale in the set
is_disjoint - not same the both set
is_subset - set from the subset of other set
is_superset - superset of specified set
'''

food = {'rice', 'idly', 'dosa'}
print("SET OF : ", food)
print("SET TYPE OF : ", type(food))

#add value in the set
food.add('biriyani')
print("added biriyani to the set :", food)

#update the value from the set
food_up_to = {'rasam', 'sambar'}
food.update(food_up_to)
print("updated  set :", food)

#pop to remove any one set value
car = {'jeep', 'swift', 'indica'}
print("pop to removed value in the set :", car.pop())
print(car)

#remove value from the set
bike = {'rx100', 'pulsar', 'tvs'}
print("removed value in the set :", bike.remove('tvs'))
print(bike)

#discard value from the set
ball = {'stemper', 'vicky', 'boost'}
print("discard to removed value in the set :", ball.discard('tennis'))
print(ball)

#union a & b merge the both set
a={1, 2, 3}
b={'a', 'b', 'c'}
c=a.union(b)

print("union of both set ", c)

#intersection of both set a and b
a={1, 2, 3, 4}
b={4, 5, 2, 6}
e = a.intersection(b)
print("intersection same value of  both a & b set ", e)

#intersection update a set in set of b
print(a)
a.intersection_update(b)
print("using intersection update in the set of a ", a)

#difference
f= {5, 6, 7}
g={7, 8, 9}
h=f.difference(g)

print("difference between set of f and g ", h)

#symmetric_difference and update
j={1, 2, 3}
k={1, 4, 5}
i=j.symmetric_difference(k)
j.symmetric_difference_update(k)
print("symmetric_difference between set of j and k ", i)
print("symmetric_difference updated set of j and k ", j)

#is_disjoint
l={1, 2, 3}
m={6, 4, 5}
n=l.isdisjoint(m)
o=l.issubset(m)
p=l.issuperset(m)
print("not same of both set value ", n)
print("l set is subset or not of set m ", o)
print("l set is superset or not of set m ", p)
