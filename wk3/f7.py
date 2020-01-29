"""
Ask the user to enter a password
that is 8 characters or long

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
message = "Password does NOT meet requirement"
if len(default) > 7:
    message = "Password meets requirement"

print(message)
