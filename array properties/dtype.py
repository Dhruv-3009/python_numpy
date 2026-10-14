# dtype is data type of the elements in the array
# dtype is returned as a string, for example: int32, float64, etc.
# syntax: array.dtype

import numpy as np

arr = np.array([10,20,30.5])
print("Array:\n", arr.dtype)