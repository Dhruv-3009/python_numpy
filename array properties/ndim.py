# ndim using for checking the number of dimensions in the array
# syntax: array.ndim
# n stands for number 
# dim stands for dimension

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([[1,2,3],[4,5,6]])
arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("Array:\n", arr1.ndim)
print("Array:\n", arr2.ndim)
print("Array:\n", arr3.ndim)