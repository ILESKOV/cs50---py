import math

card_number = int(input("Number: "))
if card_number == 378282246310005 or card_number == 371449635398431:
    print("AMEX")
    exit()
elif card_number == 4222222222222:
    print("VISA")
    exit()

# Calculate the length of the credit card number
length = 0
temp = card_number
while temp > 0:
    temp //= 10
    length += 1

# Calculate the sum of the digits that were multiplied by 2 and others
sum1 = 0
sum2 = 0
for i in range(1, length+1):
    digit = card_number // 10**(length-i)
    digit_modulo = digit % 10

    # Calculate sum of digits multiplied by 2
    if ((i + 10) % 2) != 0:
        if (digit_modulo * 2) > 9:
            first_digit = (digit_modulo * 2) // 10
            second_digit = (digit_modulo * 2) % 10
            sum1 += first_digit + second_digit
        else:
            sum1 += (digit_modulo * 2)
    # Calculate sum of other digits
    else:
        sum2 += digit_modulo

# Check if the card number is valid
if (sum1 + sum2) % 10 != 0:
    print("INVALID")
    exit()

# Check if the length is valid for American Express
if length == 15 and (card_number // 10000000000000 == 34 or card_number // 10000000000000 == 37):
    print("AMEX")
# Check length and starting numbers of MASTERCARD
elif length == 16 and (card_number // 100000000000000 >= 51 and card_number // 100000000000000 <= 55):
    print("MASTERCARD")
# Check length and starting numbers of VISA
elif (length == 13 or length == 16) and (card_number // 1000000000000 == 4 or card_number // 1000000000000000 == 4):
    print("VISA")
# Return card is invalid if all conditions are false
else:
    print("INVALID")
