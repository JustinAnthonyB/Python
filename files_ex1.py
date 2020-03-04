'''
Write the Python code to create a module named files_ex.py that includes a main() function to test all other functions. The files_ex module should have the following functions 
(use Python convention to properly name your new functions) :
a.	A function to read each line from the file and print its content line by line. The function should work if you want to print lines from a different text file too.
b.	A function that should read the entire file content as a list.
c.	A function to add the items in the following list to the file: female_oscar_win=[["Hillary Swank", 1999],["Julia Roberts", 2000],["Halle Berry", 2001], ["Nicole Kidman", 2002]
["Charlize Theron", 2003]]
d.	Re-write the above functions as new functions with an "_ex" (for exceptions) added at the end of their name. The new functions code must handle multiple exceptions as needed. 
'''

def start():
    global x
    x=""
    print("Enter file name: (most likely students.txt)")
    x = input(str(x))


def r_line_ex():
    try:
        print("a.	A function to read each line from the file and print its content line by line. The function should work if you want to print lines from a different text file too.")
        with open(x) as file:
            for line in file:
                print(line, end="") 
                print()
    except Exception as e:
        print(type(e), e)

def r_doc_ex():
    print("b.	A function that should read the entire file content as a list.")
    try:
        with open(x) as file:
            lines = file.read().splitlines()
            print(type(lines))
            print(lines)
    except Exception as e:
        print(type(e), e)


def add_item_ex():
    print("A function to add a list to the file")
    female_oscar_win = [["Hillary Swank", 1999],["Julia Roberts", 2000],["Halle Berry", 2001], ["Nicole Kidman", 2002],["Charlize Theron", 2003]] 
    try:
        with open(x, "w") as file: 
            for m in female_oscar_win:
                file.write(str(m) + "\n")
        print("Here is how the file ended up: ")
    except Exception as e:
        print(type(e), e)  
    try:
        with open(x) as file:
            for line in file:
                print(line, end="") 
                print()
    except Exception as e:
        print(type(e), e)

def main():
    start()
    r_line_ex()
    r_doc_ex()
    add_item_ex()




if __name__== "__main__":
    main()