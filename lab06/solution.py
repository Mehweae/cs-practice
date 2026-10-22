def count_by_extension(paths):
    result = {}
    for p in paths:
        name = p.split('/')[-1]
        if '.' in name:
            ext = name[name.rfind('.') + 1:].lower()
        else:
            ext = ""
        result[ext] = result.get(ext, 0) + 1
    return result

def deepest_path(paths):
    if not paths:
        return ''
    path_with_count = []
    paths = paths.sort()
    max_count = paths[0]

    for p in paths:
        count = p.count('/')
        path_with_count.append(count)
        if count > max_count:
            max_count = count
    return paths[paths.index(max_count)]

def human_size(n_bytes):
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    for unit in units:
        if n_bytes < 1024:
            if unit == "Б":
                return f"{n_bytes} {unit}"
            return f"{n_bytes:.1f} {unit}"
        n_bytes /= 1024
    return f"{(n_bytes * 1024):.1f} ТБ"