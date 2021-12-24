#getting input in python
#string input
name = input("Enter your name : ")
print("your data type is ", type(name), "your name : ", name)

#output
'''
Enter your name : parthiban
your data type is  <class 'str'> your name :  parthiban
'''
#Integer Input
age = int(input("Enter your Age"))
print("Age type is ", type(age), "your age is ", age)

'''output
Enter your Age 25
Age type is  <class 'int'> your age is  25

'''
#Floot Input
salary = float(input("Enter your salary  "))
print("data type ", type(salary), "your salary is ", salary)

'''output
Enter your salary  2000000
data type  <class 'float'> your salary is  2000000.0
'''
name_1, name_2, name_3 = input("enter your best three friends name ").split()
print("Friend one ", name_1)
print("Friend two ", name_2)
print("Friend three ", name_3)

'''output
enter your best three friends name sathish santosh sathya
Friend one  sathish
Friend two  santosh
Friend three  sathya
'''

game_1, game_2, game_3 = input("enter your best three game ").split(",")
print("Game one ", game_1)
print("Game two ", game_2)
print("Game three ", game_3)

#Multiline input
print("Enter the senetence ")
sentence = []
while True:
    line=input("Enter the word for make a sentence")
    if line:
        sentence.append(line)
    else:
        break
result = "\n".join(sentence)
print("your senence is ", result)
"""output
the 
chola 
of 
pythonist
"""
