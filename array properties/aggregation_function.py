# aggregation (sum, mean, median, min, max, var, std) 
# syntax: numpy.aggregation_function(array)

'''
np.sum(arr) - Returns the sum of array elements over a given axis.
np.mean(arr) - Returns the mean of array elements over a given axis.
np.median(arr) - Returns the median of array elements over a given axis.
np.min(arr) - Returns the minimum value of array elements over a given axis.
np.max(arr) - Returns the maximum value of array elements over a given axis.
np.var(arr) - Returns the variance of array elements over a given axis.
np.std(arr) - Returns the standard deviation of array elements over a given axis.
'''

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print("Array:", arr)

print("Sum of array elements:", np.sum(arr))
print("Mean of array elements:", np.mean(arr))
print("Median of array elements:", np.median(arr))
print("Minimum value of array elements:", np.min(arr))
print("Maximum value of array elements:", np.max(arr))
print("Variance of array elements:", np.var(arr))
print("Standard deviation of array elements:", np.std(arr))