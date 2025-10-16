# Project: Credit Card Validator
# Teclado's solution

card_number = list(input("Please enter a card number: ").strip()) # 5893804115457289

# Remove last digit
check_digit = card_number.pop()     # check_digit = 9

# Reverse number
card_number.reverse()

processed_digits: list[int] = []

for index, digit in enumerate(card_number):
    if index % 2 == 0:
        #print("Even index")
        doubled_digit = int(digit) * 2  # Double even indices

        if doubled_digit > 9:           # Then subtract 9 if > 9
            doubled_digit -= 9

        processed_digits.append(doubled_digit)

    else:
        #print("Odd index")
        processed_digits.append(int(digit))

#print(processed_digits) # [7, 2, 5, 5, 8, 5, 2, 1, 8, 0, 7, 3, 9, 8, 1]

total = sum(processed_digits) + int(check_digit)    # 80 = 71 + 9

# Finaly, verify card number: check if sum divisible by 10
if total % 10 == 0:                                 # 80 % 10 == 0 -> True
    print("Valid card number!")
else:
    print("Invalid card number!")
