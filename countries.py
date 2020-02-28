"""
•	Create a program that displays a menu which gives the user the opportunity to view, add, or delete a country from a dictionary of countries. 
The menu should also, give the user the opportunity to exit the program.  Create a function for this named display_menu().
•	Create a view()  function that begins by calling the display_codes() function to display the country codes on a single line. 
Then, it prompts the user to enter one of these codes. Next, it uses the upper() method of the string to convert the code to uppercase. 
That way, even if the user enters “mx”, the program uses “MX” as the key for the dictionary. 
This is necessary because a search done with the in keyword is case-sensitive. After making sure that the country code is uppercase, the view() function uses 
an if statement to check if the specified code is in the countries dictionary. If so, it gets the name from the dictionary and displays it. 
Otherwise, it displays a message that indicates that there’s no country for that code.
•	The add() function begins by getting a country code from the user and by converting that code to uppercase. 
Then, it checks whether the code is in the countries dictionary. If so, it prints a message that indicates that another country is already using that code. 
Otherwise, it gets a country name from the user, uses a title() method to convert that name to title case, adds the name to the dictionary, and displays an appropriate message.
•	The delete() function also begins by getting a country code from the user, converting that code to uppercase, and checking whether that code exists in the countries dictionary. 
If so, this code deletes the country from the dictionary and displays an appropriate message. Otherwise, this code displays a message that indicates that there’s no country with 
that code.
•	The main() function begins by creating a dictionary named countries that contains the codes and names for three countries. 
Then, it displays the command menu and enters the main loop for the program.
"""
def display_menu():
    print("View")
    print("Add")
    print("Delete")
    print("Exit")
    print()    

def view(countries):
    if len(countries) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        print(list(countries.values()))
        print()
        code = input (str("Enter Country Code: "))
        code = code.upper()
        if code in countries.values():
            print("yes")
            print(code)
            #  Code doesn't work, still need to display dictionary item based on user input code
            # print(countries[code]())
        else:
            print("Can't find code")
            return

def add(countries):
    country = input("Country: ")
    code = input("Code: ")
    if country in countries:
        print(str(country) + " is already added")
        return
    if code in countries:
        print(str(code) + " is already added")
        return
    else:
        countries[country.title()] = code
        # print(list(countries.items())) 
        # need to print out confirmation
        print()
    
def delete(countries):
    print(list(countries.values()))
    number = int(input("Number: "))
    if number < 1 or number > len(countries):
        print("Invalid movie number.\n")
    else:
        movie = countries.pop(number-1)
        print(movie[0] + " was deleted.\n")
        
def main():
    countries = {
        "United Kingdom":"UK",
        "America FUCK YEAH": "US",
        "CANADA": "CA"}
    
    display_menu()
    while True:        
        command = input("ENTER A COMMAND!!! ")
        command = command.upper()
        if command == "VIEW":
            view(countries)
        elif command == "ADD":
            add(countries)
        elif command == "DELETE":
            delete(countries)
        elif command == "EXIT":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
