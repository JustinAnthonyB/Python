"""
Ask the user to enter a password
Determine if password is
    Not acceptable
        less than 5 chars
    Weak
        between 5 and 7
    Medium
        between 8 and 10 chars
    Strong
        11 chars or more

Using an if statement, output whether text
meets requirement

Input from user?
    1: no, default = text
outputs(s):
    message of whether text meets requirement
data structures / sanitation:
    no. not really
"""

default = input("Enter a password. 8 char or more")
message = "Password is "
strength = "unacceptable"
password_length = len(default)

if password_length >= 5 and password_length < 8:
    strength = "weak"
elif password_length > 7 and password_length < 11:
    strength = "medium"
elif password_length > 10:
    strength = "strong"


print(message + strength)
