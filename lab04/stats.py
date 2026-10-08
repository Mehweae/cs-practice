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