# Justin Baptiste 100925081 F

'''
(10 points) A function that takes two string parameters (arguments). 
The function should then check is the first string is present as a substring in the second parameter. 
If it is found it should return its index position (beginning index and end index). 
(10 points) A function that takes a dictionary as an argument (parameter). 
The function then asks for the user input for a key (diet choice) 
and return the value of that key (measure of the average carbon footprint. 
If the diet choice is not in the dictionary, the function should display a relevant message.  
The list to be used to test this function in main is 
diet_carbon_footprint={"vegan": 955, "vegetarian": 1053, "pescatarian": 1431, "omnivorous": 2282}
(10 points) A function that takes a list and a filename as parameters then write the list to the file.
The list you can use to test this function in main is: 
myths=[ "Drinking milk can help you lose weight", "Milk is nature’s perfect food", "People need milk to be healthy". 
The file name you can use to test the function is dairy_myths.csv and has the following content:
Milk builds strong bones
Cow milk is the best source of calcium
 (10 points) Rewrite the function immediately above, rename it by ending the function name with "_ex" 
 and add all appropriate exceptions. 
(10 points) Create a main function to test the functions created above. 
Save the module in the format "LabTest2_XY_999.py" in which XY are the initials of your first and 
last name and 999 are the last 3 digits of your student number. 
'''

import csv

def f_index():
    x, y = str(input("Give me the first number: ")), (str(input("Give me the second number: ")) )
    if x in y:
        print("yes")
        index = y.index(x)
        print("The index is: " + str(index))
def diet():
    diet_carbon_footprint={"vegan": 955, "vegetarian": 1053, "pescatarian": 1431, "omnivorous": 2282}
    print(list(diet_carbon_footprint.keys()))
    print()
    print("Enter a diet: ")
    pick = input()
    if pick in diet_carbon_footprint.keys():
        x = diet_carbon_footprint.get(pick)
        print("yes, it's in the dictionary, it's value is: ")
        print(x)
    else:
        print("Can't find")
        return
def csv():
    import csv
    # A function that takes a list and a filename as parameters then write the list to the file
    pick = input("Enter a list separated by spaces: ")
    userList = pick.split()
    print("user list is ", userList)
    print("Enter file name: (most likely dairy_myths.csv)")
    x=""
    x = input(str(x))
    with open(x, "w", newline="") as file: 
        writer = csv.writer(file) 
        writer.writerows(userList)

def csv_ex():
    import csv
    import sys
    try:
        # A function that takes a list and a filename as parameters then write the list to the file
        pick = input("Enter a list separated by spaces: ")
        userList = pick.split()
        print("user list is ", userList)
        print("Enter file name: (most likely dairy_myths.csv)")
        x=""
        x = input(str(x))
        with open(x, "w", newline="") as file: 
            writer = csv.writer(file) 
            writer.writerows(userList)
    except Exception as e:
        print(type(e), e)
    except FileNotFoundError as e: 
        print("FileNotFoundError:", e) 
        sys.exit() 

def main():
    diet_carbon_footprint={"vegan": 955, "vegetarian": 1053, "pescatarian": 1431, "omnivorous": 2282}
    f_index()
    diet()
    csv()
    csv_ex()

if __name__== "__main__":
    main()