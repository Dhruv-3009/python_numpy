# astype() method is used to cast a numpy array to a different data type.
import numpy as np

arr = np.array([1.0, 2.8, 3.3, 4.4, 5.6])
print("Original Array:", arr)

arr_int = arr.astype(int)
print("Array after converting to int:", arr_int)
print("Data type of the new array:", arr_int.dtype)