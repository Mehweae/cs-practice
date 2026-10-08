import sys
from stats import average_by_city, read_valid, warmest_city, parse_record

lines = sys.stdin.read().splitlines()
count_of_valid_lines = 0
count_of_errors = 0
for line in lines:
    cleaned = line.strip()
    if not(cleaned):
        continue
    try:
        parse_record(cleaned)
        count_of_valid_lines += 1
    except ValueError:
        count_of_errors += 1
valid = read_valid(lines)
warm_city = warmest_city(valid)
avg_by_warm_city = average_by_city(valid)[warm_city]

print(f'{count_of_valid_lines}\n{count_of_errors}\n{avg_by_warm_city}')