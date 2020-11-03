import math

n = int(input())

max_value = 0
max_snow = 0
max_time = 0
max_quality = 0

for i in range (n):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    value = (snowball_snow / snowball_time) ** snowball_quality
    # value = math.pow((snowball_snow / snowball_time), snowball_quality)
    if value > max_value:
        max_value = value
        max_snow = snowball_snow
        max_time = snowball_time
        max_quality = snowball_quality
print(f"{max_snow} : {max_time} = {int(max_value)} ({max_quality})")