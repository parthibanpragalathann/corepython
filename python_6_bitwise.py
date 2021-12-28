"""
bitwise operators are utilized to perform bitwise estimations on whole numbers.
The numbers are first changed over into binary and afterward activities are performed on bit by bit,
thus the name bitwise operators.
"""
# Bitwise Operators

"""
& 	AND	each bit is 1 it's True others False 
|	OR	any one bit is 1 it's true both bit are not same is False
 ^	XOR	any one bit is 0 it's true both bit are same is False
~ 	NOT	Inverts all the bits
<<	Zero fill left shift, let the leftmost bits fall off
>>	Signed right shift let the rightmost bits fall off
"""
bit_val_a=50
bit_val_b=10

print("AND BITWISE OPERATOR 50 & 10 ", bit_val_a & bit_val_b)
print("OR BITWISE OPERATOR 50 | 10 ", bit_val_a | bit_val_b)
print("XOR BITWISE OPERATOR 50 ^ 10 ", bit_val_a ^ bit_val_b)
print("NOT BITWISE OPERATOR ~ 50 ", ~bit_val_a)
print("left shift BITWISE OPERATOR  10 << 2 ", bit_val_b << 2)
print("right shift BITWISE OPERATOR 50 >> 2 ", bit_val_a >> 2)