import numpy as np
#numpy 2.0.2

#Заданвие 1
hours = np.arange(0, 24, 3)
line = np.arange(0, 1.1, 0.2)
zeros = np.vectorize(int)([0] * 6)
unknown_table = np.matrix([[-1, -1, -1]] * 2)
identity = np.identity(3, int)

print(hours, hours.shape, hours.ndim, hours.size, hours.dtype)

