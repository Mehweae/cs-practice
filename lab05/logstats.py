
def parse_event(line) :
    '''Парсим и резолвим строчку'''
    first = line.find(" ")
    second = line.find(" ", first + 1)
    return {"time": line[:first].strip(),"level": line[first + 1 : second].strip(),"message": line[second + 1 :]}

def count_levels(lines):
    '''Разбиваем строчку на виды ошибок'''
    out = {"BROKEN": 0, "DEBUG": 0, "ERROR": 0, "INFO": 0, "WARNING": 0}
    for i in lines:
        parsed_item = parse_event(i)
        match parsed_item["level"]:
            case "INFO":
                out["INFO"] += 1
            case "WARNING":
                out["WARNING"] += 1
            case "ERROR":
                out["ERROR"] += 1
            case "DEBUG":
                out["DEBUG"] += 1
            case _ :
                out["BROKEN"] += 1
    return out
