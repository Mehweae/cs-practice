def parse_record(line: str) -> dict:
    if len(line.split(";")) != 3:
        raise ValueError(f"Incorrect data format.: {line}")
    city, temp_str, date = line.split(";")
    if not city or not date
        raise ValueError(f"Incorrect data format.: {line!r}")
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Incorrect data format.: {line!r}")
    return {"city": city, "temp": temp, "date": date}

def read_valid(lines: list[str]) -> list[dict]:
    valid_lines = []
    for line in lines:
        try:
            valid_lines.append(parse_record(line))
        except ValueError:
            pass
    return valid_lines