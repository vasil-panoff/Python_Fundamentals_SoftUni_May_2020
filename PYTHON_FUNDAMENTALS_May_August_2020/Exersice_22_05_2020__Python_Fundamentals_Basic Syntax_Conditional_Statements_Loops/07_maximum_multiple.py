lst = []
first_num = int(input())
second_num = int(input())
num = 0

for num in range (first_num, second_num + 1):
    if num % first_num == 0 and num <= second_num and num > 0:
        lst.append(num)
print(max(lst))
