# item = someSortOfSelection()
# if item in myList:
#     doMySpecialFunction(item)

# movie_list=[[1,2,3,4],[1]]

movie_list =[ ['a','b'], ['a','c'], ['b','d'] ]

# year = int(input("give me a year "))
# for item in movie_list:
#     if year in item:
#         print(item[0])

# choice = int(input("give me a year... YOU FILTHY ANIMAL "))
# j=0
# for i in movie_list:
#     j = j + 1
#     while j > len(choice) and choice in i:
#         print(i[0]) 
choice = (input("give me a year... YOU FILTHY ANIMAL "))
for i in range (0, len(movie_list)):
    if movie_list[i][1]==choice:
       found=1
       print(movie_list[0])