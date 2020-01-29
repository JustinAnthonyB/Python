#!/usr/bin/env python3
import search

def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        i = 1
        for row in movie_list:
            # added additional row
            print(str(i) + ". " + row[0] + " (" + str(row[1]) + ")" + " (" + str(row[2]) + ")")
            i += 1
        print()

def add(movie_list):
    name = input("Name: ")
    year = input("Year: ")
    # added price here
    price = input("Price: ")

    movie = []
    movie.append(name)
    movie.append(year)
    # added price here
    movie.append(price)
    movie_list.append(movie)
    print(movie[0] + " was added.\n")   

def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number-1)
        print(movie[0] + " was deleted.\n")

# created this search func



    #           Not my code

    # year = int(input("give me a year "))
    # for item in movie_list:
    #     if year in item:
    #         print(item[0])


            
            
            
            


def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    # added search option
    print("search - search you filthy animal")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    

def main():
    movie_list = [["Monty Python and the Holy Grail", 1975, 20],
                  ["On the Waterfront", 1954, 20],
                  ["Cat on a Hot Tin Roof", 1958, 20]]

    display_menu()

    while True:        
        command = input("Command: ")
        if command == "list":
            list(movie_list)
        elif command == "add":
            add(movie_list)
        elif command == "search":
            search.search(movie_list)
        elif command == "del":
            delete(movie_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
