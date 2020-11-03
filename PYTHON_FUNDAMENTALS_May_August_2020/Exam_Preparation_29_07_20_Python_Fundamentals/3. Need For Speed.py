n = int(input())

plants_info = {}

for i in range(n):
    data = input().split("<->")
    plant = data[0]
    mileage = int(data[1])
    fuel = int(data[2])

    cars[car] = {}
    cars[car]["mileage"] = mileage
    cars[car]["fuel"] = fuel

data = input()
while "Exibition" != input_command:
    tokens = input_command.split(" : ")
    command = tokens[0]
    car = tokens[1]

    if "Drive" == command:
        distance = int(tokens[2])
        fuel = int(tokens[3])
        if cars[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["fuel"] -= fuel
            cars[car]["mileage"] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car]["mileage"] >= 100000:
                print(f"Time to sell the {car}!")
                del cars[car]

    elif "Refuel" == command:
        fuel = int(tokens[2])
        current_fuel = cars[car]["fuel"]
        fuel_to_fill = 0
        if current_fuel + fuel <= 75:
            cars[car]["fuel"] += fuel
            fuel_to_fill = fuel
        else:
            fuel_to_fill = 75 - cars[car]["fuel"]
            cars[car]["fuel"] = 75
        print(f"{car} refueled with {fuel} liters")
    elif "Revert" == command:
        distance_to_revert = int(tokens[2])
        if cars[car]["mileage"] - distance_to_revert < 10000:
            cars[car]["mileage"] = 10000
        else:
            cars[car]["mileage"] -= distance_to_revert
            print(f"{car} mileage decreased by {distance_to_revert} kilometers")

    input_command = input()

sorted_cars = sorted(cars.keys(), key=lambda c:(-cars[c]["mileage"], c))
for x in sorted_cars:
    print(f"{x} -> Mileage: {cars[x]['mileage']} kms, Fuel in the tank: {cars[x]['fuel']} lt.")
