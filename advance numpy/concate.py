'''
concat() method is used to join two or more arrays along an existing axis
syntax: numpy.concatenate((arr1, arr2, ...), axis=0)

axis = 0 vertical concatenation (row-wise)
axis = 1 horizontal concatenation (column-wise)
'''

import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

new_arr = np.concatenate((arr1, arr2), axis=0)
print("Array after concatenation along axis 0:\n", new_arr)
