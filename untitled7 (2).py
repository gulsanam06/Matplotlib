# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QAIPfcJnmH59FjinZSx_fY66qKgU6gGw
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,8])
y=np.array([0,250])
plt.plot(x,y)i
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,8])
y=np.array([0,250])
plt.plot(x,y,'+')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([2,4,7,10])
y=np.array([3,8,1,6])
plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,8,1,6])
plt.plot(y,'o:r')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,8,1,6])
plt.plot(y,marker='o',ms=20,
mec='g')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x1=np.array([0,1,2,4])
x2=np.array([3,5,8,10])
y1=np.array([6,7,11,5])
y2=np.array([0,1,3,2])
plt.plot(x1,y1,x2,y2)
plt.show()