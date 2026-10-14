'''
np.split() -> equal
np.hsplit() -> horizantlly
np.vsplit() -> vertically
'''

import numpy as np

arr = np.array([1,2,3,4,5])
print("original array", arr)

print("Split array:")
print(np.split(arr, 5))