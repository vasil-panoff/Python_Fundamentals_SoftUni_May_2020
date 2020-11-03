cost = int(input())
number_months = int(input())

savings_per_month = cost * 0.25
total_savings = 0
souveniers_money = 0
cloates = 0
bonus = 0
for i in range(1, number_months + 1):
    if i % 3 == 0:
        cloates = savings_per_month - (savings_per_month * 0.16)
    if i % 4 == 0:
        bonus = savings_per_month - (savings_per_month * 1.25)

    savings_per_month += savings_per_month

souveniers_money = total_savings + bonus - cloates - cost
if total_savings > cost:
    print(f"Bravo! You can go to Disneyland and you will have {souveniers_money:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {abs(souveniers_money):.2f}lv. more.")
