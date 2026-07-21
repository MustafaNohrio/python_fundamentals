import numpy as np

#to check
print(np.__version__)  #2.5.1 

my_list = [1, 2, 3, 4, 5]
my_list =my_list * 2
print(my_list)  #[1, 2, 3, 4, 5, 1, 2, 3, 4, 5] it duplicated every element

array = np.array([1, 2, 3, 4, 5])
print(array)    #[1 2 3 4 5]
#to check if it is a numpy array
print(type(array))  #<class 'numpy.ndarray'>

array = array * 2
print(array)    #[ 2  4  6  8 10] > every element got multiplied by 2


