'''

A logical operator is a symbol, Logical operators are used on conditional statements (either True or False).
used to connect two or more expressions. Common logical operators include AND, OR, and NOT.

'''

# Logical Operators in Python
log_val_a = 10
log_val_b = 0
print("10 is greater than 20 and 0 is greater than 10\n using OR operator to check IF True or False\n The Result is :  ", log_val_a>20 and log_val_b>20)
print("10 is less than 20 or 0 is greater than 10\n using OR operator to check IF True or False\n The Result is :  ", log_val_a<20 or log_val_b>20)
print("0 is not greater than 10\n using NOT operator to check IF True or False\n The Result is :  ", not log_val_b>20)

