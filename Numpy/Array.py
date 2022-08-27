# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 20:08:30 2022

@author: ASUS
"""

import numpy as np

#the repeat an array

arr = np.array([1, 2, 3])

r1 = np.repeat(arr, 4, axis=0)

print(r1)
print("\n")
# a matrix create

output = np.ones((5, 5))

print(output)

z = np.zeros((3, 3))

z[1, 1] = 9

print(z)

print("\n")

output[1:-1, 1:-1] = z #create final matrix

print(output)


