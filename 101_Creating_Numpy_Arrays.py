# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 14:44:07 2024

@author: prash
"""

import numpy as np

#Creating array

my_1d_array = np.array([1, 2 , 3])

type(my_1d_array)

#Shape

my_1d_array.shape

#Accessing the element
my_1d_array[0]

#Slicling
my_1d_array[0:2]

#Negative Indexing

my_1d_array[-1]

my_2d_array =np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(my_2d_array)

my_2d_array.shape

#accessing 2d array elements

my_2d_array[0]
my_2d_array[1]


my_2d_array[0][1]
my_2d_array[0,1]

#Slicing 2d array
my_2d_array[0:2,1:3]



np.zeros(3)

np.zeros((3,3))

np.zeros((3,3,3))


np.ones(3)

np.full((3,3), 5)



np.arange(10)

np.arange(2,10)

np.arange(2,10,2)


np.linspace(1, 5,20)

float_array = np.linspace(1, 5,20)

np.round(float_array,2)



np.random.rand(10)

np.random.rand(5,2)

np.random.randint(20,80,100)

np.random.randint(20,80,(10,10))


my_1d_array = np.random.randint(20,80,100)

my_2d_array = my_1d_array.reshape(10,10)
print(my_2d_array)


