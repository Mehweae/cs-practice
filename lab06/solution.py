def count_by_extension(paths):
    extension_count = {}
    for path in paths:
        filename = path.split('.')[-1].lower()
        if filename:
            extension_count[filename] = extension_count.get(filename, 0) + 1
        else:
            extension_count[""] = extension_count.get("", 0) + 1
    return extension_count

def deepest_path(paths):
    if not paths:
        return ''
    max_deep = max(p.count('/') for p in paths)
    return min(p for p in paths.sort() if p.count('/') == max_deep)

def human_size(n_bytes):
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    for unit in units:
        if n_bytes < 1024:
            if unit == "Б":
                return f"{n_bytes} {unit}"
            return f"{n_bytes:.1f} {unit}"
        n_bytes /= 1024
    return f"{(n_bytes * 1024):.1f} ТБ"