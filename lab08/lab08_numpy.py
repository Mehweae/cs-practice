import numpy as np
#numpy 2.0.2

#Заданвие 1
hours = np.arange(0, 24, 3)
line = np.linspace(0,1,5)
zeros = np.vectorize(int)([0] * 6)
unknown_table = np.matrix([[-1, -1, -1]] * 2)
identity = np.identity(3, int)

print(hours, hours.shape, hours.ndim, hours.size, hours.dtype)

#Задание 2
print(hours[2], hours[-1], hours[2:5], hours[::2], hours[::-1], sep = "\n")

#Задание 3
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
print(temperatures.shape, temperatures.ndim, temperatures.size, temperatures[1, 2], temperatures[0], temperatures[:, -1],\
      temperatures[:2, 1:],temperatures[:2, 1:3], sep = "\n")

#Задание 4
matrix = np.arange(1, 26).reshape(5, 5)

def print_matrix(matrix):
    print(matrix, matrix.shape)

print_matrix(matrix[:2])
print_matrix(matrix[-2:])
print_matrix(matrix[:, :2])
print_matrix(matrix[1:4, 2:5])
print_matrix(matrix[-2:, -2:])


