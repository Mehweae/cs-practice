def parse_record(line: str) -> dict:
    if line:
        if len(line.split(";")) != 3:
            raise ValueError(f"Incorrect data format.: {line}")
        city, temp_str, date = line.split(";")
        if not city or not date or not temp_str:
            raise ValueError(f"Incorrect data format.: {line!r}")
        try:
            temp = float(temp_str)
        except ValueError:
            raise ValueError(f"Incorrect data format.: {line!r}")
        return {"city": city, "temperature": temp, "date": date}

def read_valid(lines: list[str]) -> list[dict]:
    valid_lines = []
    for line in lines:
        try:
            valid_lines.append(parse_record(line))
        except ValueError:
            pass
    return valid_lines

def average_by_city(records: list[dict]) -> dict:
    sum_by_city = {}
    count_by_city = {}
    for record in records:
        sum_by_city[record["city"]] = sum_by_city.get(record["city"], 0) + record["temperature"]
        count_by_city[record["city"]] = count_by_city.get(record["city"], 0) + 1
    avg_by_city = {}
    for city in sum_by_city:
        avg_by_city[city] = sum_by_city[city] / count_by_city[city]
    return avg_by_city

def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)
    if not averages:
        return ""
    best_city = ""
    best_avg = -float("inf")
    for city in sorted(averages):
        if averages[city] > best_avg:
            best_city = city
            best_avg = averages[city]
    return best_city