'''
Write the Python code to create a module named files_ex.py that includes a main() function to test all other functions. The files_ex module should have the following functions 
(use Python convention to properly name your new functions) :
a.	A function to read each line from the file and print its content line by line. The function should work if you want to print lines from a different text file too.
b.	A function that should read the entire file content as a list.
c.	A function to add the items in the following list to the file: female_oscar_win=[["Hillary Swank", 1999],["Julia Roberts", 2000],["Halle Berry", 2001], ["Nicole Kidman", 2002]
["Charlize Theron", 2003]]
d.	Re-write the above functions as new functions with an "_ex" (for exceptions) added at the end of their name. The new functions code must handle multiple exceptions as needed. 
'''



def r_line():
    x=""
    print("Pick a file to read line by line: ")
    x = input(str(x))
    with open(x) as file:
        for line in file:
            print(line, end="") 
            print()

def r_doc():
    x=""
    print("Pick a file to read into a list: ")
    x = input(str(x))
    # with open(x) as file: 
    #     x = file.readlines() 
    #     print(x[0], end="") 
    #     print(x[1])
    #     print(x[:])
    #     print(x)
    with open(x) as file:
        lines = file.read().splitlines()
        print(type(lines))
        print(lines)



def add_item():
    x=""
    print("Pick a file to add a list to: ")
    x = input(x)
    # members = ["John Cleese", "Eric Idle"]
    female_oscar_win = [["Hillary Swank", 1999],["Julia Roberts", 2000],["Halle Berry", 2001], ["Nicole Kidman", 2002],["Charlize Theron", 2003]] 
    with open(x, "a") as file: 
        for m in female_oscar_win:
            file.write(str(m) + "\n")
    with open(x) as file:
        for line in file:
            print(line, end="") 
            print()


# def new_thing() << this is number d.


def main():
    r_line()
    r_doc()
    add_item()




if __name__== "__main__":
    main()