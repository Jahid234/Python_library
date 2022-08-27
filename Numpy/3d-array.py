# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 20:27:40 2022

@author: ASUS
"""

import numpy as np

b = np.array([[[1, 2], [3, 4], [5, 6], [7, 8]]])

print(b)

print("\n")

#get a specific element (work outside in)
print(b[0, 1, 1])

print("\n")

#replace

b[:, 1, :] = [9, 9]

print(b)

#Creating different types of array 

#all 0s matrix

x = np.zeros((2, 3))

print(x)

#all 1s in matrix

print("\n")

y = np.ones((4, 4, 3))  # 4 = matrix number, 4 = matrix raw, 3 = matrix column

print(y)

#any other number

z = np.full((2, 2), 99)
print(z)

#any other (full_like)

A = np.full_like(b, 4) #full_like = full matrix changes by specific number

print(A)





