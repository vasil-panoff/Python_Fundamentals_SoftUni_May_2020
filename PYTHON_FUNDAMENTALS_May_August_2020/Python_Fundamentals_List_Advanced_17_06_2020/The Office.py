employees = input().split(" ")
happiness_factor = int(input())
employees = # Use map to multiply each element with the factor
filtered = # Use filter to get all the numbers >= than the average
if len(filtered) >= len(employees) / 2:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are not happy!")
