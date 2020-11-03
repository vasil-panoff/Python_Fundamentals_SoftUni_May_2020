n = int(input())
capacity = 255

total_litres = 0
for i in range (n):
    litres = int(input())
    if total_litres + litres > capacity:
        print("Insufficient capacity!")
    else:
        total_litres += litres
print (total_litres)