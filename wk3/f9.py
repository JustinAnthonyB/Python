"""
Display values 1-5
    using a loop
        in 3 distinct ways
"""

# while loop
counter = 1
while counter <=5:
    print(counter)
    counter += 1
print()

# for loop, using range
for item in range(1, 6):
    print(item)
print()

one_to_five = list(range(1, 6))

for number in one_to_five:
    print(number)
print()
