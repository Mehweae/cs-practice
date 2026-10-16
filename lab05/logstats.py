
def parse_event(line) :
    '''Парсим и резолвим строчку'''
    first = line.find(" ")
    second = line.find(" ", first + 1)
    return {"time": line[:first].strip(),"level": line[first + 1 : second].strip(),"message": line[second + 1 :].strip()}
