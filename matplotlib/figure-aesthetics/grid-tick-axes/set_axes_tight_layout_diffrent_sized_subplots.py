# The tight_layout automatically adjusts different sized multiple subplots parameters into the figure area.
import matplotlib.pyplot as plt
import numpy as np


# Generate mock data
# Fixing random state for reproducibility
np.random.seed(100000)

# Make up some data in the interval (0, 1)
# Draw random samples from a normal (Gaussian) distribution.
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))


def linear_plot(ax):
    ax.plot(x, y)
    ax.set_yscale('linear')
    ax.set_xlabel('x-label', fontsize=10)
    ax.set_ylabel('y-label', fontsize=10)
    ax.set_title('Linear', fontsize=12)


ax1 = plt.subplot(221)
ax2 = plt.subplot(223)
ax3 = plt.subplot(122)

linear_plot(ax1)
linear_plot(ax2)
linear_plot(ax3)

plt.tight_layout()
plt.savefig('set_axes_tight_layout_different_sized_subplots.pdf')
plt.show()
