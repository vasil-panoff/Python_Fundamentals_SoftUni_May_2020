number = int(input())

while True:
    year = str(number+1)
    if len(set(year)) == len(year):
        print(year)
        break

    number += 1