# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:19:10 2022

@author: Matthias
"""

import matplotlib

# matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
import numpy as np

print("Display plot in backend:", matplotlib.get_backend())
x = np.arange(0,2*np.pi,0.01)
y = np.cos(x)

plt.plot(x,y)

plt.show()