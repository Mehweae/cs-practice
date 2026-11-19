from typing import List

import numpy as np

def make_hours() -> list[float] :
    return [i for i in range(0, 23, 3)]

def vector_report(values:list[float]) -> dict:
    return {"third": values[2], "last": values[-1], "middle": values[2:6], "every_second": values[::2], "reversed": values[::-1]}

def change_vector(values: list[float]) -> list[float]:
    val = np.asarray(values).copy()
    val[2:5] = 99
    val[::2] = -1
    return val.tolist()

def cap_above(values: list[float], limit: float) -> list[float]:
    res = np.asarray(values).copy()
    mask = res > limit
    res[mask] = limit
    return res.tolist()

def celsius_to_fahrenheit(values:list[float]) -> list[float]:
    return (np.asarray(values, dtype= float) * 9/5 + 32).tolist()
