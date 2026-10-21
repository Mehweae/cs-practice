def count_by_extenson(paths):
    extenson_count = {}
    for path in paths:
        filename = path.split('.')[-1].lower()
        if filename:
            extenson_count[filename] = extenson_count.get(filename, 0) + 1
        else:
            extenson_count[""] = extenson_count.get("", 0) + 1
    return extenson_count
def deepest_path(paths):
    ...
def human_size(n_bytes):
    ...