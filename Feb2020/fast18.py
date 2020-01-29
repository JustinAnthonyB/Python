#Finding Unique Elements in a String

my_string = "aavvccccddddeee"

# converting the string to a set
temp_set = set(my_string)

# stitching set into a string using join
new_string = ''.join(temp_set)

print(new_string)

# Reversing a string using slicing

my_string = "ABCDE"
reversed_string = my_string[::-1]

print(reversed_string)

# Output
# EDCBA

n = 3 # number of repetitions

my_string = "abcd"
my_list = [1,2,3]

print(my_string*n)
# abcdabcdabcd

print(my_list*n)
# [1,2,3,1,2,3,1,2,3]