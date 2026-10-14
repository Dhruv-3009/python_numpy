'''
append() method is used to add values 
syntax: numpy.append(arr, values, axis=None)
'''

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr)

# append
arr = np.append(arr, [6, 7, 8])
print("Array after appending [6, 7, 8]:", arr)