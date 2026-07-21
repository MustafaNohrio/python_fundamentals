import numpy as np

# zero dimensional array
array = np.array('A')
print(array.ndim)   #0 >(ndim) = n dimensions

# one dimensional array
array1 = np.array(['A', 'B', 'C'])
print(array1.ndim)  #1
print(array1.shape)  #(3,)

# two dimensional array
array2 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(array2.ndim)  #2
print(array2.shape) #(3, 3)

# three dimensional array
array3 = np.array([[[1,  2,  3], [4,  5,  6], [7,  8,  9]],
                  [[10, 11, 12],[13, 14, 15],[17, 18, 19]],
                  [[21, 22, 23],[24, 25, 26],[27, 28, 29]]])
print(array3.ndim)  #3
print(array3.shape)  #(3, 3, 3)