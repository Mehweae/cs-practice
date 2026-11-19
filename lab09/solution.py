from typing import List

import numpy as np

def make_hours() -> list[int] :
    return list(np.arange(0, 24, 3))

def vector_report(values:list[float]) -> dict:
    return {"third": values[2], "last": values[-1], "middle": values[2:6], "every_second": values[::2], "reversed": values[::-1]}

def change_vector(values: list[float]) -> list[float]:
    val = np.asarray(values).copy()
    val[2:5] = 99
    val[::2] = -1
    return list(val)

def cap_above(values: list[float], limit: float) -> list[float]:
    res = values.copy()
    mask = values > limit
    res[mask] = limit
    return res

def celsius_to_fahrenheit(values:list[float]) -> list[float]:
    return values * 9/5 + 32