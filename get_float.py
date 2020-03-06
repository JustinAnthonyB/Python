def get_float():
    low = 0.0
    high = 10.0
    choice = float((input("Give me a float between " + str(low) + "and " + str(high) + " ")))
    print()
    if choice:
        choice = str(choice)
        print((choice) + " is correct")
    else:
        print((choice) + " is not-correct")
    get_float()
def main():
    
    get_float()

if __name__== "__main__":
    main()