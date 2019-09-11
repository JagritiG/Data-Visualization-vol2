# matplotlib can display plot titles centered, flush with the left side
# of a set of axes, and flush with the right side of a set of axes.
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

# Plot log scale
plt.figure()
plt.plot(x, y)
plt.yscale('log')
plt.title('Log', loc='center', pad=15, fontsize=16, color='b',  fontweight='semibold', style='normal', family='serif')

plt.savefig('set_title.pdf')
plt.show()

