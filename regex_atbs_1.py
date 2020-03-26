'''
Author: Justin Baptiste
This is the first RegEx exercise from ATBS
'''


# This First Function (isPhoneNumber) is equal to the second function
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
          print('Phone number found: ' + chunk)
          foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers')

print('******')

# These are equal to above
import re

# For on Phone number
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())

print('******')

# For all phone numbers
mo1 = phoneNumRegex.findall(message)
print(mo1)


