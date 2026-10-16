
def parse_event(line) :
    '''Парсим и резолвим строчку'''
    line = line.strip()
    parts = line.split(maxsplit=2)
    if len(parts) == 3:
        return {"time": parts[0], "level": parts[1], "message": parts[2]}
    else:
        raise ValueError("Inavlid format")

def count_levels(lines):
    '''Разбиваем строчку на виды ошибок'''
    out = {"BROKEN": 0, "DEBUG": 0, "ERROR": 0, "INFO": 0, "WARNING": 0}
    for i in lines:
        line = i.rstrip("\n")
        if not line.strip():
            continue
        try:
            parsed_item = parse_event(i)
            try:
                out[parsed_item["level"]] += 1
            except KeyError:
                out["BROKEN"] += 1
        except ValueError:
            out["BROKEN"] += 1
    return out

def top_errors(lines: list[str], n: int):
    '''Находим топ по ошибок по уровню error'''
    out = []
    for i in lines:
        line = i.rstrip("\n")
        if not line.strip():
            continue
        try:
            parsed_item = parse_event(i)
            if parsed_item["level"] == "ERROR":
                flag = False
                for message in out:
                    if parsed_item["message"] == message[0]:
                        flag = True
                        message[1] += 1
                        break
                if not flag:
                    out.append([parsed_item["message"], 1])
        except ValueError:
            pass
    return sorted(out, key=lambda x: (-x[1], x[0]))[:n]

def format_report(counts: dict, errors: list[list]):
    '''Формируем отчёт по данным'''
    report = "Отчёт по журналу\n\n"
    levels_sorted = sorted(counts[0].items())
    for i in levels_sorted:
        report.append(f"{i}: {counts[i]}\n")
    report.append("\nЧастые ошибки:\n")
    list_of_top_errors = top_errors(errors, 3)
    for i in list_of_top_errors:
        report.append(f"- {i[0]} - {i[1]}")
    return report