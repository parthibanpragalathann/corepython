# Delete a File in Python


# To delete a file, you must import the OS module, and run its os.remove() function.

# Source Code
import os

if os.path.exists("data.txt"):
    os.remove("data.txt")
else:
    print("File Not Found")
