import sys
from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
valid = read_valid(lines)
count_of_lines = len(lines)
count_of_valid_lines = len(valid)

warm_city = warmest_city(valid)
warm_city_temps = []
for i in valid:
    if warm_city == i:
        warm_city_temps.append(i)
avg_by_warm_city = average_by_city(warm_city_temps)

print(f'{count_of_lines}\n{count_of_lines - count_of_valid_lines}\n{avg_by_warm_city}')