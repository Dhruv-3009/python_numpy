'''
array[index] 1d array
array[row, column] 2d array
array[row, column, depth] 3d array
'''

import numpy as np

arr = np.array([1, 2, 3, 7, 8, 9])

print("Original Array:\n", arr[0])
print("Original Array:\n", arr[3])
print("Original Array:\n", arr[-1])