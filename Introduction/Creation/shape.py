# defualt values
# syntax: np.zeros(shape, dtype=float, order='C')

import numpy as np

arr = np.zeros(3)
print("Array:\n", arr)


# ones (shape)

arr_once = np.ones((3, 4))
print("Array:\n", arr_once)


# full (shape, fill_value)

arr_full = np.full((2, 3), 7)
print("Array:\n", arr_full)
