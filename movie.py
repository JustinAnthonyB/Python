#!/usr/bin/env python3

from object import Movie

# BB doesn't accept two files
# class Movie:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year

#     def getStr(self):
#         return 'Name: {} Year: {}'.format(self.name, self.year)

def list(movie_list):
    for i in range(len(movie_list)):
        print(movie_list[i].getStr())

def add(movie_list):
    name = input("Name: ")
    year = input("Year: ")
    movie_list.append(Movie(name,year))

def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        print("The following has been deleted:\n")
        print(movie_list[number-1].getStr())
        movie_list.pop(number-1)
      
def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    

def main():
    movie_list = [Movie("Monty Python and the Holy Grail", 1975),
                Movie("On the Waterfront", 1954),
                Movie("Cat on a Hot Tin Roof", 1958)]

    display_menu()
    
    while True:        
        command = input("Command: ")
        if command == "list":
            list(movie_list)
        elif command == "add":
            add(movie_list)
        elif command == "del":
            delete(movie_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()

