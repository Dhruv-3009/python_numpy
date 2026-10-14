'''
--> 1d array: [1, 2, 3, 4, 5]
delete() method is used to delete elements
syntax: numpy.delete(arr, obj, axis=None)
'''

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr1)

# delete
new_arr1 = np.delete(arr1, 4)
print("Array after deleting element at index 4:", new_arr1)

'''
-->2d array: [[1, 2, 3], [4, 5, 6]])
syntax: numpy.delete(arr, obj, axis=None)
'''

arr2 = np.array([[7, 8, 9], [2, 4, 6]])
print("Original Array:\n", arr2)

new_arr2 = np.delete(arr2, 0, axis=0) 
print("Array after deleting element at index 5 along axis 0:\n", new_arr2)