"""
1. Complete the following exercise by writing the python code:
Have the user enter a word (the secret word)
Then simulate a letter guessing game by having the user enter a letter and the program returning a relevant notice if the letter is found and another notice if the letter is not found. Repeat the game while user is still interested in playing.
Write 2 versions of this solution: one without writing your own functions and one with functions.

2.	Modify exercise 1 to add the following:
•	Create a list of words. You can copy some words from http://www.free-teacher-worksheets.com/
•	Import random module and make use of the choice function from random module to select a string from your list of words. This randomly selected string is your secret word.
•	Then continue with the letter guessing game as described in ex 1.

3.	Modify the exercise 2 to add the following:
•	Validate the user input for the letter guessed to ensure that the user does not enter more than a letter or a blank space.

4.	Modify exercise 3 to add the following:
•	Keep track of all letters guessed and do not let the user try the same letter more than once.
"""
import random
import sys

def main():
    a_list = ("alpha", "beta", "gamma", "zeta", "epsilon", "omega")
    answer = random.choice(a_list)
    corr_ans=0
    s_list = []
    c_list = []
    while True:
        secret = input("Give a guess! You have 20 tries, or type exit to leave ")
        if secret == "exit":
            sys.exit()
        if secret in s_list[:]:
                print('You already guessed that')
                corr_ans = corr_ans - 1
        if secret.isalpha() and len(secret) == 1:
            s_list.append(secret)
            if secret in answer:
                corr_ans = corr_ans + 1
                print("Correct! ")
                c_list.append(secret)
            if corr_ans == -20:
                print("You Lose, the answer is " + answer)
                print(s_list[:])
                sys.exit()
            if c_list == answer:
                print("You Win, the answer is " + answer)
                print(s_list[:])
                sys.exit()
        else:
            print("wrong")
            corr_ans = corr_ans - 1

if __name__== "__main__":
    main()