# boolean masking selecting elements based on a condition true or false

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("original array:", arr)

# boolean masking
print("boolean masking:", arr[arr > 2])