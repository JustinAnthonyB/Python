import sys

def collatz(number):
    global count
    count = 0
    while number != 1:
        if number % 2 == 0: # EVEN
            number = number//2
            print(number)
            count = count +1
        elif number % 2 ==1: # ODD
            number = 3 * number + 1
            print(number)
            count = count +1

number = int(input("Give me a number. Or type exit to quit "))
if number == "exit":
    sys.exit()
else:
    collatz(number)
    print("the number " + str(number) + " has " \
        + str(count) + " iteration(s) of collatz before hitting 1")
    
        

