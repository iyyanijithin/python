# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:59:00 2020

@author: jithin
"""

import numpy as np
import pandas as pd

data = pd.read_csv('Data.csv')

print(np.__version__)
arr = np.array([1,2,3,4])
print(type(arr))


arr2 = np.array([1,2,3,4,5,6])
arr3 = np.array(([1,2],[3,4]))

print(arr2.ndim)
print(arr3.ndim)

print(arr2[0])
print(arr3[1,1])

#Slicing
#First is where we start
#Second is the size till we have to go
print(arr2[1:2])
#Start from index 1o till the end
print(arr2[1:])

print(arr2[:3])

print(arr2[-3:-1])

print(arr2[:4:2])

#[start Index:Stop Index : Counter]


arr4 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(arr4[1,1:3])

print(arr4[:,2])
print(arr4.dtype)

#Create a copy 
arr5 = arr2.copy()

#Create a referec
arr6 = arr2.view()

print(arr6.shape)


arr7 = np.array([1,2,3,4,5],ndmin=5)
print(arr7.shape)
