# Project: Credit Card Validator

# Luhn algorithm
# aka "modulus 10" or "mod 10" algorithm

# Starting number:
card_num = input("Enter card number: ").replace(" ", "")  # e.g., 5893804115457289
print(card_num)

card_number = [int(n) for n in card_num]    # Convert str to int & put in list
print(card_number)

# Remove last digit aka check digit:
check_digit = card_number.pop()
print(card_number)

# Reverse remainding digits:
# Note: `reversed` is lazy.
reversed_num = list(reversed(card_number))      # Alt: `card_number.reverse()`
print(reversed_num)

# Double digits at even indices:
digits_doubled: list[str] = [] # Can only append str; not int

for index, digit in enumerate(reversed_num):
    if index % 2 == 0:
        digit = (digit * 2)
        #print("Even index")
    else:
        digit = digit * 1
        #print("Odd index")

    digits_doubled.append(str(digit))
    #print(digits_doubled)       # Check ea iteration

print(", ".join(digits_doubled))

# Subtract 9 if over 9:
dig_doubled = [int(n) for n in digits_doubled]

sub_9: list[str] = []

for dig in dig_doubled:
    if dig > 9:
        dig -= 9
    else:
        dig = dig

    sub_9.append(str(dig))

print(", ".join(sub_9))     # print values
print(sub_9)                # print values as strings in a list

print()

# Add ea digit, including the removed/check digit:
'''
sub_9_int = [int(n) for n in sub_9]
sum_dig = 0
for sub in sub_9_int:
    sum_dig += sub
'''
# or
'''
sub_9_int = [int(n) for n in sub_9]
sum_dig = sum(n for n in sub_9_int)
'''
# or
sum_dig = sum(list(int(n) for n in sub_9)) # Only 1 line of code

sum_final = sum_dig + check_digit

print(sum_dig)
print(sum_final)


# If sum divisible by 10, `card_num` is a valid card number:
if sum_final % 10 == 0:
    print(f"Your card number, {card_num}, is valid.")
else:
    print(f"Your card number, {card_num}, is NOT valid.")



