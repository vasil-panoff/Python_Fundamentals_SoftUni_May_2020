def get_odd_even_sums(number):
    even_total = 0
    odd_total = 0

    number_lenght = len(number)
    for num in range(1, number_lenght):
        
        if i % 2 == 0:
            even_total = even_total + num
        else:
            odd_total = odd_total + num

    return (f"Odd sum = {odd_total}, Even sum = {even_total}")

number = input()
output = get_odd_even_sums(number)
print(output)