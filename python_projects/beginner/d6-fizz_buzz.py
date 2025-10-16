# Project: Fizz Buzz

# Instructions:
# Start counting from 1.
# Fizz: number divisible by 3
# Buzz: number divisible by 5
# Fizz Buzz: number divisible by 3 and 5
# Stop at a specified number, e.g., 100 in this case.
#
# Knowledge required: print, for loop, range, conditional, Boolean, modulo
#
print("# Fizz Buzz")
# Code:
numbers = list(range(1, 101))
for number in numbers:
    if number % 3 == 0 and number % 5 == 0:     # alt: if number % (3*5) == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


# Output:
'''
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
Fizz Buzz
...
98
Fizz
Buzz
'''

print()

# Notes
print("# notes".title())
# You need to put the more specific conditions first. Since the numbers divisible by `3*5` are a smaller subset than the others (`3`, `5`), the condition checking for divisibility by `3*5` needs to be put first.
#
# modulo operator:
# The modulo operator (%) outputs the remainder of a division.
# remainder: the number which is left undivided after division.
# If x is divisible by y, then the remaindedr will be 0.
# This does not output the quotient (result of division); it outputs the remainder.
# Syntax: dividend % divisor
# Read: <Dividend> divided by <divisor> has a remainder of <output>.
#
# Expression    # Output (Remainder)
print(3 % 3)    # 0
print(5 % 3)    # 2
print(5 % 5)    # 0
print(15 % 3*5) # 0     
