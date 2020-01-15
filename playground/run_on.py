import sys

def comma(items):
    for i in range(len(items) -2):
        print(items[i] + ', ', end="")
    print(items[-2] + ' and ' + items[-1]) 


answer = input("Give me some items for a list (no spaces) or type exit to quit ")
if answer == "exit":
    sys.exit()
else:
    comma(answer)


