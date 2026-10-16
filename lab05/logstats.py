from unittest import case


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
    out = {}
    for i in lines:
        line = i.rstrip("\n")
        if not line.strip():
            continue
        try:
            parsed_item_level = parse_event(i).get("level")
            if parsed_item_level == "DEBUG":
                if "DEBUG" in out:
                    out["DEBUG"] += 1
                else:
                    out["DEBUG"] = 1
            elif parsed_item_level == "ERROR":
                if "ERROR" in out:
                     out["ERROR"] += 1
                else:
                    out["ERROR"] = 1
            elif parsed_item_level == "INFO":
                if "INFO" in out:
                    out["INFO"] += 1
                else:
                    out["INFO"] = 1
            elif parsed_item_level == "WARNING":
                if "WARNING" in out:
                    out["WARNING"] += 1
                else:
                    out["WARNING"] = 1
            else:
                if "BROKEN" in out:
                    out["BROKEN"] += 1
                else:
                    out["BROKEN"] = 1
        except ValueError:
            out["BROKEN"] += 1
    return out
print(count_levels([]))
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
    levels_sorted = sorted(counts.items())
    for i in levels_sorted:
        report = report + (f"{i[0]}: {i[1]}\n")
    report = report + ("\nЧастые ошибки:\n")
    list_of_top_errors = errors[:3]
    for i in list_of_top_errors:
        report = report + (f"- {i[0]} — {i[1]}\n")
    return report