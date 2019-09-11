# Resizing axes with constrained layout
# Resize subplots in a figure so that there are no overlaps between axes objects and labels on the axes.
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


def linear_plot(ax):
    ax.plot(x, y)
    ax.set_yscale('linear')
    ax.set_xlabel('x-label', fontsize=10)
    ax.set_ylabel('y-label', fontsize=10)
    ax.set_title('Linear', fontsize=12)


# Plot without using constrained_layout, the labels overlap the axes
fig, axs = plt.subplots(nrows=2, ncols=2, constrained_layout=False)

for ax in axs.flat:
    linear_plot(ax)


plt.savefig('set_axes_without_constrained_layout.pdf')

# Plot using constrained_layout=True
fig, axs = plt.subplots(nrows=2, ncols=2, constrained_layout=True)

for ax in axs.flat:
    linear_plot(ax)

plt.savefig('set_axes_with_constrained_layout.pdf')
plt.show()
