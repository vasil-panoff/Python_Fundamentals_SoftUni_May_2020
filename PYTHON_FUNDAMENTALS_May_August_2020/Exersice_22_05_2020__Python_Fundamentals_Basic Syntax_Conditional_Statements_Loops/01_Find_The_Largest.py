num = input()
num = str(num)

arr_digits = []


def findMaxNum(digits):
    digits.sort(reverse=True)
    number = ''.join(digits)

    return number


for digit in range(len(num)):
    arr_digits.append(num[digit])

print(findMaxNum(arr_digits))