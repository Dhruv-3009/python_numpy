# operations without using for loop

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr)

# Element-wise addition
arr_add = arr + 10
print("Array after adding 10:", arr_add)

# Element-wise multiplication
arr_mul = arr * 2
print("Array after multiplying by 2:", arr_mul)

# Element-wise exponentiation
arr_pow = arr ** 2
print("Array after squaring each element:", arr_pow)
