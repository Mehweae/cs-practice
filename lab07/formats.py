import csv
import json

def csv_to_records(text):
    reader = csv.reader(text.splitlines(), delimiter=',')
    return [dict(s) for s in reader]

def _strip_comment(text):
    pos = text.find('#')
    return text[:pos].strip() if pos != -1 else text.strip()

def _parse_scalar(value):
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
        return value[1:-1]
    low = value.lower()
    if low in ('true', 'yes'):
        return True
    if low in ('false', 'no'):
        return False
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass
    return value

def parse_settings(lines):
    settings = {}
    current_list_key = None

    for raw_line in lines:
        line = raw_line.rstrip('\n')
        stripped = line.strip()

        if not stripped:
            continue

        indent = len(line) - len(line.lstrip(' '))

        if indent == 0:
            if stripped.startswith('#'):
                continue
            key, _, value = stripped.partition(':')
            key = key.strip()
            value = _strip_comment(value)
            if value == '':
                current_list_key = key
                settings[key] = []
            else:
                settings[key] = _parse_scalar(value)
                current_list_key = None
        else:
            if current_list_key is not None and stripped.startswith('-'):
                item = _strip_comment(stripped[1:])
                if item:
                    settings[current_list_key].append(_parse_scalar(item))

    return settings