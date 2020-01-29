
my_list_1 = list("hello")

# my_list_2 = my_list_1
# my_list_2 = my_list_1.copy()
# my_list_2 = my_list_1[:]
my_list_2 = my_list_1[0:len(my_list_1)]
my_list_1.append(".")


print(my_list_1, my_list_2, sep="\n")
