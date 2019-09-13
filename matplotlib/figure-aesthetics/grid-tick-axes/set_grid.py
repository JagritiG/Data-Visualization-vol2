# Adding grids
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(10000)

# Make up some data in the interval (0, 1)
# Draw random samples from a normal (Gaussian) distribution.
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))


plt.figure()

# Plot a Linear scale
plt.plot(x, y, label='Linear')
plt.yscale('linear')
plt.title('Linear')
plt.xlabel('x label')
plt.ylabel('y label')
plt.grid(color='lightgray', linestyle='--', linewidth='0.5')

plt.legend()
plt.savefig('set_grid.pdf')
plt.show()



