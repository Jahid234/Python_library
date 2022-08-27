# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 19:54:24 2022

@author: ASUS
"""

import numpy as np

a = np.array([1, 2,3])
print(a)

b = np.array([1, 3, 5])
print(b)

print(a*b)

#Get dimension using ndim

c = np.array([[1, 2, 3], [1, 2, 3], [1, 2,3]])

print(c.ndim)


#get shape

print(c.shape)

#get type

print(c.dtype)

#get size

print(c.itemsize)

#get total size

print(c.nbytes)

