# B5 Prog02: Ask user number input (0-1000). Print in 6 digit format
# Add zeroes at the beginning to complete the 6 digit

"""
PSEUDOCODE

User input
print input with a function to add zero
"""

user = int(input("Enter number (0-1000): "))
print(str(user).zfill(6))