'''
syntax: array[start:stop:step]
negative indexing syntax: array[-start:-stop:-step]
'''

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Original Array:\n", arr[1:5])  # index 1 to 4 (5 is not included)
print("Original Array:\n", arr[:5])  # the beginning up to index 5 (5 is not included)
print("Original Array:\n", arr[::2])  # all elements with step 2
print("Original Array:\n", arr[::-1])  # all elements in reverse order