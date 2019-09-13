# The tight_layout automatically adjusts subplot parameters into the figure area.
import matplotlib.pyplot as plt
import numpy as np

# Generate mock data
# Fixing random state for reproducibility
np.random.seed(10000)

# Make up some data in the interval (0, 1)
# Draw random samples from a normal (Gaussian) distribution.
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))


def linear_plot(ax, fontsize):
    ax.plot(x, y)
    ax.set_yscale('linear')
    ax.locator_params(nbins=3)
    ax.set_xlabel('x-label', fontsize=fontsize)
    ax.set_ylabel('y-label', fontsize=fontsize)
    ax.set_title('Linear', fontsize=fontsize)


plt.close('all')

# Plot without tight_layout
fig, axs = plt.subplots()
linear_plot(axs, 24)
plt.savefig('set_axes_without_tight_layout.pdf')

# Plot with tight_layout
fig, axs = plt.subplots()
linear_plot(axs, 24)
plt.tight_layout()

plt.savefig('set_axes_with_tight_layout.pdf')
plt.show()
