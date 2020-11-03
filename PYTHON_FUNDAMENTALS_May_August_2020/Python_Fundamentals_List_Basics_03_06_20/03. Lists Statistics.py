n = int(input())

positive_numbers = []
negatives_numbers = []

for _ in range(n):
    number = int(input())
    if number >= 0:
        positive_numbers.append(number)
    else:
        negatives_numbers.append(number)

count_positives = len(positive_numbers)
sum_of_negatives = sum(negatives_numbers)

print(positive_numbers)
print(negatives_numbers)
print(f"Count of positives: {count_positives}. Sum of negatives: {sum_of_negatives}")