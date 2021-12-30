'''
Nested for loop in python

nested loop refers to a loop within a loop

'''

#Write a program to print * to ***** line by line
for i in range(6):
    for j in range(i):
        print("*", end="") #end is used to print
    print()

#output
'''
*
**
***
****
*****
'''


#Write a program reverse to print * to ***** line by line
for i in range(6, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

#output
'''
******
*****
****
***
**
*
'''

#A-Z = 65 - 90
#a-z =97 - 122

for i in range(65, 71, 1):
    for j in range(65, 71, 1):
        print(chr(j), end="")
    print()

'''
ABCDEF
ABCDEF
ABCDEF
ABCDEF
ABCDEF
ABCDEF
'''

for i in range(97, 101, 1):
    for j in range(97, 101, 1):
        print(chr(j), end="")
    print()

"""
abcd
abcd
abcd
abcd
"""

#write a program to using else in while and for loop
'''
python provides else in the looping concepts loop completed properly we can use else block also executed
'''
i=0
while i<5:
    print(i)
    i+=1
else:
    print("while loop is completed")

for i in range(1, 6, 1):
    print(i)
else:
    print("For loop is completed")

#output
"""
0
1
2
3
4
while loop is completed
1
2
3
4
5
For loop is completed

"""
