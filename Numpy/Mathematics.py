# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 20:15:27 2022

@author: ASUS
"""

import numpy as np

a = np.array([[1, 2, 3, 4], [2, 3, 4, 5]], dtype=('float32'))

print(a)

print("\n")

print(a+2)
print("\n")

print(a-2)
print("\n")

print(a*2)
print("\n")

print(a/2)
print("\n")


b = np.array([1, 0, 1, 0])

print(a+b)

#Take the sin

print("\n")

print(np.cos(a))