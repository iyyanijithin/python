#Will  show how to use numpy

import numpy as np

#Crete 1 d array
arr1 = np.array([10,20,30])
print(arr1)
print(type(arr1))

arr2 = np.array([[1,2,3] ,[4,5,6]])
print(arr2)
print(arr2.shape)

#Create a 5 by 5 array
arr3 = np.zeros((5, 5))
print(arr3)

arr4 = np.ones((5,5),dtype=np.int)
print(arr4)

