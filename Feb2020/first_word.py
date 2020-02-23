# How to get the first word in a string 

title = input("Give me a movie title and I will give you the first letter! ")
print()
i = title.find(" ") 						 
if i == -1:
	first_word=(title + " doesn't contain a space.")
else: 
    first_word = (title[0:i] + " is the first word of " + title)

print(first_word)