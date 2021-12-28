"""
ELIF STATEMENT IN PYTHON
sometimes there are more than two possibilities one way to computation we can use elif
If true then the indent statement get executed.
elif true then the indent statement get executed.
else If&elif is not True/False executed else part.
"""
#write a program to check programmer Quality get name, programming language and points
name = input("Enter your name : ")
language = input("Enter your programming language : ")
points = int(input("Enter your points out of 10 : "))

if points < 5:
    print(name, "You become a Intermediate in the", language+" program")
elif points < 8:
    print(name, "You become a Expert in the", language+" program")
else:
    print(name, "You become a Expert in the", language+" program")
'''
condition IF is True output 
Enter your name : parthiban
Enter your programming language : python
Enter your points out of 10 : 6
parthiban You become a Expert in the  python program


condition ELIF is True output
Enter your name : joshva
Enter your programming language : java
Enter your points out of 10 : 4
joshva You become a Intermediate in the  java program


condition IF/ELIF is not True/False output
Enter your name : irfan
Enter your programming language : ruby
Enter your points out of 10 : 10
irfan You become a Expert in the  ruby program
'''
