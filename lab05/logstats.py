from operator import truediv
from sys import flags


def parse_event(line) :
    '''Парсим и резолвим строчку'''
    line = line.strip()
    parts = line.split(maxsplit=2)
    if len(parts) == 2:
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
            out[parsed_item["level"]] += 1
        except ValueError:
            out["BROKEN"] += 1
    return out

def top_errors(lines: list[str], n: int):
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
