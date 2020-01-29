text = "Hello World"

for letter in text:
    print(letter)

my_list_1 = [1, True, False, 12.344, "boo"]

for item in my_list_1:
    print(item)
print()

for item in range(len(my_list_1)):
    print("The index of {} has a value of {}"
          .format(item, my_list_1[item]))
print()

