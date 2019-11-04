# 3D Surface plot
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

plt.style.use('seaborn')


X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.cos(R)

fig = plt.figure(figsize=(10, 5))
ax = Axes3D(fig)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.plasma)
ax.set_title('3D Surface Plot', font_param)


# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.savefig('surface3d.pdf')
plt.show()
