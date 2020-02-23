"""
1. Complete the following exercise by writing the python code:
Have the user enter a word (the secret word)
Then simulate a letter guessing game by having the user enter a letter and the program returning a relevant notice if the letter is found and another notice if the letter is not found. Repeat the game while user is still interested in playing.
Write 2 versions of this solution: one without writing your own functions and one with functions.
"""
import random
import sys

def main():
    answer = "abc"
    corr_ans=0
    while True:
        secret = input("Give a guess! OR type exit to leave ")
        if secret == "exit":
            sys.exit()
        if secret.isalpha() and len(secret) == 1:
            if secret in answer:
                corr_ans = corr_ans+1
                print("great ")
                print(corr_ans)
        


# while True:
#     print('Type exit to exit.')
#     response = input()
#     if response == 'exit':
#         sys.exit()
#     print('You typed ' + response + '.')
        # print("correct")
# Using the in keyword to search a string
# spam = "Congratulations. You've won a million dollars." 
# "million" in spam 		# True
# "Million" in spam 		# False - search is case-sensitive
# "on" in spam			# True – doesn't need to be whole word
# " million " in spam 		# True – uses spaces to find a whole word
    else:
        print("wrong")

    # if type(secret) == type(int):
    #     print("wrong input")
    # else:
    #     if type(secret) == type(str):
    #         print("good work")


main() 