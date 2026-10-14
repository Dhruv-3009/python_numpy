'''
Reshape defines a new shape for an array without changing its data.
syntax: numpy.reshape(array, newshape)
if dimension match 
Reshaping not create a copy of the original array
it returns a view of the original array whenever possible.
'''

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print("Original Array:", arr)
reshaped_arr = np.reshape(arr, (2, 3))
print("Reshaped Array:\n", reshaped_arr)
