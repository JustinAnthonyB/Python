'''
Author: Justin Baptiste
This is the second RegEx exercise from ATBS
'''
import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print("group one is " + mo.group(1))
print("group two is " + mo.group(2))
print("group 0 is " + mo.group(0))
print("group () is " + mo.group())

print('******')

phoneNumRegex1 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo1 = phoneNumRegex1.search('My phone number is (415) 555-4242.')
print("group one with parentheses is " + mo1.group(1))

print('******')

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo2 = batRegex.search('Batmobile lost a wheel')
print("group () is " + mo2.group())
print("group one is " + mo2.group(1))
