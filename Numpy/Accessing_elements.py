# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 20:10:01 2022

@author: ASUS
"""

import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8,9, 10, 11, 12, 13, 14]])

print(a)

#get a specific element(r, c)

print(a[1, 6])

#get a specific row

print(a[0, :])

#get a specific column

print(a[:, 2])

#get a specific little more fancy [startindex:endindex:stepsize]

print(a[0, 1:-2:2])

#assign a value / replacing

a[1, 5]=20
a[:, 2]=[1, 2]

print(a)