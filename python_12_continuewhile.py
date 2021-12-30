'''

Continue using while loop in python

continue statement used to move the control towards the top of the next iteration in the loop.
it's used both while and for loop.

'''

#write the program to print the add number using continue statement
i=1
while i<=10:
    if i % 2==0:
        i=i+1
        continue
    print(i, "this is add number ")
    i+=1


