import numpy as np

# three dimensional array
array3 = np.array([[[1,  2,  3], [4,  5,  6], [7,  8,  9]],
                  [[10, 11, 12],[13, 14, 15],[17, 18, 19]],
                  [[21, 22, 23],[24, 25, 26],[27, 28, 29]]])
print(array3.ndim)  #3
print(array3.shape)  #(3, 3, 3)

print(array3[0, 0, 0])  #1
print(array3[0, 2, 0])  #1
print(array3[2, 0, 0])  #1