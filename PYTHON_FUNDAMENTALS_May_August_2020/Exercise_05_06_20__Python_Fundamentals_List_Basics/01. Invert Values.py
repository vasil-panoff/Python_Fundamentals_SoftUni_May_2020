text = input()

number_str = text.split()
numbers = []

for num_str in number_str:
    number = -int(num_str)
    numbers.append(number)

print(numbers)
