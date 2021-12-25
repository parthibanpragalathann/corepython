'''
STRINGS IN PYTHON
A String is a sequence of character, it is defined with in the single or double quotes.


'''
fruit = "banana"
print("data type is ", type(fruit)) #get the type of data
print("data location is ", id(fruit)) #get the location of data
print("data length is ", len(fruit)) #get the length of data using len()

#Traversal with while and for loop in string
print("iter data using for loop")
for char in fruit:
    print(char)

prefix="MKS"
suffix="aran"
for letter in prefix:
    print(letter+suffix)

#STRING SLICE
'''A segment of astring is called a slice'''
segment = "string"
print(segment[1:4])
print(segment[-3:-1])
print(segment[1:])
print(segment[:3])
print("reverse string ", segment[::-1])

#STRING SEARCH
'''traversing a sequence and returning when we find we are looking for its called search'''
def finding(word, letter):
    index=0
    while index<len(word):
        if word[index]==letter:
            print(index)
        index+=1
    print("searching letter of d index is  ", index)
finding("abcdef", letter='d')

#string character count using for loop
count=0
for i in fruit:
    if i=="a":
        count+=1
print("looping count of A is ", count)

#string methods
str_val="banana"
str_vall="BAT"
print("banana convert into upper case ", str_val.upper()) #all text convert into upper
print("BAT convert into lower case ", str_vall.lower()) #all text convert into lower
print("banana convert into capitalize ", str_val.capitalize()) #text convert into capitalize
print("banana convert into title ", str_val.title()) #text convert into title
print("a character count in banana ", str_val.count("a")) #text count in the string
print("ab character endswith in banana ", str_val.endswith("ab")) #text endswith check ab in the end of the string
print("a character find in banana ", str_val.find("a")) #text find to check a in the string
print("a character find in banana ", str_val.find("a", 5)) #text find to check a index 5 in the string
print("a character replace in o ", str_val.replace("a", "o")) #text replace a to o in the string
print("banana check isupper ", str_val.isupper()) # text check isupper
print("banana check islower ", str_val.islower()) # text check islower
print("banana check isalpha ", str_val.isalpha()) # text check isalpha
print("banana check isalnum ", str_val.isalnum()) # text check isalnum
split_str = "I \nbecome\n a \nIndustrialist"
print(split_str)
print("split the line of the string ", split_str.splitlines()) #split the line of the string
print("split the line of the string ", split_str.splitlines(True)) #split the line of the string without loss data
strip_text = "  john    "
print("strip the text ", strip_text.strip()) #strip the text whitespace removed
print("left strip the text ", strip_text.lstrip()) #strip the text left side whitespace removed
print("right strip the text ", strip_text.rstrip()) #strip the text right side whitespace removed
date = "20-30-2021"
print("partition the text -  ", date.partition("-")) #partition the text -


'''output of string
data type is  <class 'str'>
data location is  2388998572848
data length is  6
iter data using for loop
b
a
n
a
n
a
Maran
Karan
Saran
tri
in
tring
str
reverse string  gnirts
3
searching letter of d index is   6
looping count of A is  3
banana convert into upper case  BANANA
BAT convert into lower case  bat
banana convert into capitalize  Banana
banana convert into title  Banana
a character count in banana  3
ab character endswith in banana  False
a character find in banana  1
a character find in banana  5
a character replace in o  bonono
banana check isupper  False
banana check islower  True
banana check isalpha  True
banana check isalnum  True
I 
become
 a 
Industrialist
split the line of the string  ['I ', 'become', ' a ', 'Industrialist']
split the line of the string  ['I \n', 'become\n', ' a \n', 'Industrialist']
strip the text  john
left strip the text  john    
right strip the text    john
partition the text -   ('20', '-', '30-2021')

'''