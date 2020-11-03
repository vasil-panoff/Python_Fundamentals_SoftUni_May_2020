YEARS_IN_CENTURY = 100
DAYS_IN_YEAR = 365.2422
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60


centuries = int(input())
years = (centuries * YEARS_IN_CENTURY)
days = int(years * DAYS_IN_YEAR)
hours = (days * HOURS_IN_DAY)
minutes = (hours * MINUTES_IN_HOUR)
seconds = (minutes * SECONDS_IN_MINUTE)

print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes = {seconds} seconds")