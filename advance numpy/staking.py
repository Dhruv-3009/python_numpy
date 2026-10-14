'''
--> staking 
vertically = vstack() row wise
horizontally = hstack() column wise
'''

import numpy as np

arr1 = np.array([1,2,3,4,5])
print("original array", arr1)

arr2 = np.array([6,7,8,9,10])
print("original array", arr2)

print(np.vstack((arr1, arr2)))
print(np.hstack(((arr1, arr2))))
