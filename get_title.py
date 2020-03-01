def get_title():
    name_list=("Mrs","Mr","Ms", "Dr", "prof")
    print(name_list[:])
    choice = (input("Give me your title "))
    if choice in name_list:
        print("correct")
    else:
        print("wrong")
    get_title()
def main():
    get_title()

if __name__== "__main__":
    main()