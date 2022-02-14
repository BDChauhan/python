
# from pandas import array

from numpy import *
arr = array([
        [1,2,3],
        [4,5,6],
        [7,8,9]
])
print(arr)
print(arr.dtype,"dimensions: ", arr.ndim,"Shape:", arr.shape,"Size:", arr.size)

# convert n-D array to 1D array
arr2 = arr.flatten()
print(arr2)

# 1D to nD
arr3 = arr2.reshape(3,3)
print(arr3)

arr3 = arr2.reshape(3,3,1) #try (1,3,3), (3,1,3)
print(arr3)

# Matrix

m = matrix(arr)
m2 = matrix('1 1 1; 2 2 2; 3 4 5')
print(m)
print("Diagonal: ", diagonal(m))
print(m.min(), m.max())

# multiplication of two matrices

# addition
m3 = m + m2
print(m3)

m3 = m * m2 #so simple!
print(m3)