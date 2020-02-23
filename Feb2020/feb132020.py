# An iterative function that sums all numbers from zero to an upper limit 
def add_numbers(upper): 
    total = 0
    for number in range(upper + 1): 
        total += number
        return number

# A recursive function that does the same thing 
def add_numbers(upper): 
    if upper == 0: 
        return upper
    else: 
        return upper + add_numbers(upper - 1)


# Common recursive algorithms

# A recursive function that calculates the factorial of a number 
def factorial(num): 
    if num == 0: 
        return 1
    else: 
        return num * factorial(num - 1)



# An iterative function that calculates the factorial of a number 
def factorial(num): 
    fact = 1
    for number in range(1, num+1): 
        fact = number * fact
        return fact


# The Fibonacci series 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, ...

# A recursive function that calculates a Fibonacci series 
def fib(n):
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return fib(n - 1) + fib(n - 2)


print(fib(12))

