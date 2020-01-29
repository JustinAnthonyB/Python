import random
md_list = [[1, 2, 3], [-2, 4, 7], [5, 6, 10]]
print(md_list)
random.shuffle(md_list)
print(md_list)
print()
random_list = random.choice(md_list)
print(random_list)
random_value = random.choice(random_list)
print(random_value)
