'''
--> 1d array: [1, 2, 3, 4, 5]
insert() method is used to insert values into a numpy array at specified indices.
syntax: numpy.insert(arr, obj, values, axis=None)
arr: Input array
obj: Index or indices before which values is inserted. 
values: Values to be inserted into arr. It can be a single value or an array of values.
axis = 0 then row wise
axis = 1 then column wise
'''

import numpy as np

arr = np.array([1,2,4,5,6,7,8,9])
print("Original Array:\n", arr)

new_arr = np.insert(arr, 2, 3) # inserting 3 at index 2
print("Array after inserting 3 at index 2:\n", new_arr)

'''
-->2d array: [[1, 2, 3], [4, 5, 6]])
'''

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Original Array:\n", arr)

new_arr = np.insert(arr, 2, [7,8,9], axis=0)
print("Array after inserting [7,8,9] at index 2 along axis 0:\n", new_arr)