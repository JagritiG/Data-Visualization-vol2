# Simple colorbar
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np

ax = plt.subplot()
im = ax.imshow(np.arange(100).reshape((10, 10)),  cmap='RdBu_r')

# create an axes on the right side of ax. The width of cax will be 7%
# of ax and the padding between cax and ax will be fixed at 0.25 inch.
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="7%", pad=0.25)

plt.colorbar(im, cax=cax)
ax.set_title("Colormap", size=12, fontweight='semibold')

plt.tight_layout()
plt.savefig('colormap.pdf')
plt.show()
