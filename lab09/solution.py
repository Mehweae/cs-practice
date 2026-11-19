import numpy as np

def make_hours():
    return np.arange(0, 24, 3)

def vector_report(values):
    return {"third": values[2], "last": values[-1], "middle": values[2:6], "every_second": values[::2], "reversed": values[::-1]}

def change_vector(values):
    val = values.copy()
    val[2:5] = 99
    val[::2] = -1
    return val

def cap_above(values, limit):
    res = values.copy()
    mask = values > limit
    res[mask] = limit
    return res