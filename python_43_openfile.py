#Open a File in Python
# File handling is an important part of any web application. Python has several functions for creating, reading, updating, and deleting files.


# File Handling
# The key function for working with files in Python is the open() function. This function takes two parameters; filename, and mode.


# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# Source Code
try:
    f=open("content.txt",'w')
    #f=open("data.txt",'a')
    #f=open("data.txt",'r')
    #print(f.read())
    #print(f.readline())
    """
    for line in f:
        print(line)
    """
    f.write("\nThis is New Line")
except FileNotFoundError:
    print("File not Found")
else:
    print("Thank You")
    f.close()






