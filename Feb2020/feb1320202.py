# 1.Create a validation module name the file validation.py The module should have a main() 
# function to test the functions in it. The validation module should  include the following functions:

# get_pos_int()
def main():
    # x=get_pos_int()
    # print(x)
    # y=get_float()
    # print(y)
    z=get_title()
    print(z)
# a. A get_pos_int() function that accepts user inputs for an integer greater than zero. 
# The user should be prompted to enter a value until the value entered meets the above mentioned 
# requirements (integer and greater than  zero)
def get_pos_int():
    while True:
        num = input("Enter a positive number: ")
        if num.isdigit() and int(num) > 0:
            return num
        else:
            print("re-enter")

# b. A get_float() function that accepts the user input for a float value between 
# a low and a high range. The user should be prompted to enter a value until the value 
# entered meets the above-mentioned requirements (float, greater than the low and lower than the high)
def get_float():
    while True:
        pick=input("Give a float between 1.0 and 10.0\n")
        if pick.isdecimal():
            if (float(pick) < 10.0 and float(pick) > 1.0):
                return pick
            else:
                print("re-enter")
# c. A get_title() function that accepts user input for a string representing the user title which 
# should be one of the following values: Mrs., Mr., Ms., Dr., Prof.
def get_title():
    while True:
        titles=["Mrs","Mr"]
        title=input("Type in your title: ")
        if title.isalpha() and title in titles:
            return title
        else:
            print("wrong") 

# d. A tuple_list_stats() function that has a tuple of integers or a list of integers as a parameter 
# and returns the average, minimum, maximum of the values in the tuple of list as well as 
# the number of duplicates. The function should also print the elements in an ascending or 
# descending order.
# e. A function that takes a list of strings as a parameter and prints out the elements sorted in ascending and descending order. Make sure to take in consideration the letter case of the list elements. Give a meaningful name to your function that follows Python naming convention for functions. 
# f. A function that calculates the sum of numbers from 1 to x where x is specified when the function is called in main function. You must complete this function recursively.
# g. A function that takes a list of integers as a parameter and returns the element with the maximum value. You must complete this function recursively.
# h. A function that returns how many digits a positive integer has. You must complete this function recursively. Remember that we can calculate the number of digits by repeatedly dividing the integer to 10 without keeping the remainder until the number is less than 10 (therefore consisting of one digit only). Add 1 to this value for each time we divide by 10. When testing this function in main use the following test values: 13, 103, 13903.
# 2. Import the validation.py module into a new module and test each function. 

if __name__ == "__main__":
        main()