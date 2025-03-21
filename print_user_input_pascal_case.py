# B5 Prog09: Ask user to input fullname with incorrect casing
# Print input in pascal case

"""
PSEUDOCODE

ask user input
print in pascal case using functions: split() and title()
"""

user = input("Enter Fullname (incorrect casing): ").title()
print(user.replace(" ", ""))