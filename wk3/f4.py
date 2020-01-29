tup_1 = tuple("hello")

print("H" in tup_1)

print(len(tup_1))

print(tup_1[-3])

print(tup_1[:3])
# starting (inc), ending (excl), step
print(tup_1[::2])

tup_2 = tup_1 * 3
print(tup_2)

# tup_1[1] = "A"
print(tup_1[1])

let_1, let_2, let_3, let_4, let_5 = tup_1
print(let_1, let_2, let_3, let_4, let_5)

let_1 = 12
print(let_1, let_2, let_3, let_4, let_5)

a1 = list(range(1, 3))
a, b = a1
print(a, b)
