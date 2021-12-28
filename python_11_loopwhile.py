'''

Loop is a Repeated execution of a set of statements.
Increment is an update that increase the value of a variable
Decrement is an update that decrease the value of a variable
Initialize an assignment that given the initial value to a variable will be updated
'''
#write a program to print 1 to 5 numbers using while loop
i=1
while i<=5:
    print(i)
    i+=1
'''
Output
1
2
3
4
5
'''
#write a program to bam blast in 8 seconds using while loop with else
i=8
while i > 0:
    print("bam blast in ", i, "seconds ")
    i-=1
else:
    print("bam blasted")
'''
bam blast in  8 seconds 
bam blast in  7 seconds 
bam blast in  6 seconds 
bam blast in  5 seconds 
bam blast in  4 seconds 
bam blast in  3 seconds 
bam blast in  2 seconds 
bam blast in  1 seconds 
bam blasted
'''
#write a program to check even or add
n=int(input("enter the number to check add or even : "))
while n!=1:
    if n % 2==0:
        print(n, "is a even number")
        break
    else:
        print(n, "is a add number")
        break
else:
    print("given value is not valid put the value above 1")

'''
condition True output
enter the number to check add or even : 4
4 is a even number

condition is false
enter the number to check add or even : 1
given value is not valid put the value above 1
'''
