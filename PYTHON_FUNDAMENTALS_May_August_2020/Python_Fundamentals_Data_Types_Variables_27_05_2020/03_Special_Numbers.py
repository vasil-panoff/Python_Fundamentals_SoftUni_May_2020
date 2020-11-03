n = int(input())

for number in range(1, n + 1):
    sum_of_digits = 0

    number_copy = number
    while number_copy > 0:
        digit = number_copy % 10
        sum_of_digits += digit
        number_copy = int(number_copy / 10)

    is_special_number = sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11
    print(f'{number} -> {is_special_number}')

# simple solution:

n = int(input())

for number in range(1, n + 1):
    sum_of_digits = 0
    for chr in str(number):
        sum_of_digits += int(chr)
    is_special_number = sum_of_digits in (5,7,11)
    print(f'{number} -> {is_special_number}')