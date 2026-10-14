'''
.ravel () -> view
.flatten () -> copy
'''

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Original Array:\n", arr)

# flattening the array
flattened_arr = arr.flatten()
print("Flattened Array:\n", flattened_arr)

# ravel of the array
ravel_arr = arr.ravel()
print("View Array:\n", ravel_arr)
