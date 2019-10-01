# 3D Bar Plot
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.style.use('seaborn')

# Prepare data
_x = np.arange(5)
_y = np.arange(6)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

# setup the figure and axes
fig= plt.figure()
ax = fig.add_subplot(111, projection='3d')

top = x + y
bottom = np.zeros_like(top)
width = depth = 1

ax.bar3d(x, y, bottom, width, depth, top, color='lightblue')
ax.set_title('3D Bar Plot', size=12, fontweight='semibold')

plt.tight_layout()
plt.savefig('bar3d.pdf')
plt.show()

