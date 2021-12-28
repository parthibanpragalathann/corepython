"""
IF ELSE STATEMENT IN PYTHON
the Boolean statements expression after is called condition If true then the indent statement get executed.
if is not executed else part.
"""
#write a program to check vote eligibility get name and age (he/she)
name = input("Enter your name : ")
age = int(input("Enter your age : "))
if age > 18:
    print(name, "Your Eligible to vote")
else:
    print(name, "Not Eligible to vote")

'''
condition is True output 
Enter your name : parthiban
Enter your age : 24
parthiban Your Eligible to vote
condition is not True/False output
Enter your name : john
Enter your age : 12
john Not Eligible to vote 
'''
