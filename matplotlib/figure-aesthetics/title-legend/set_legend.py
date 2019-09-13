# Setting legends
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 10)

fig, ax = plt.subplots()

# note that plot returns a list of lines.  The "l1, = plot" usage
# extracts the first element of the list into l1 using tuple
# unpacking.  So l1 is a Line2D instance, not a sequence of lines
l1, = ax.plot(x, x, color='C4', linestyle=':', linewidth=3, dash_capstyle='round', dash_joinstyle='round')
l2, = ax.plot(x, x**2, c='C2', ls='--', lw=2.5, dash_capstyle='projecting', dash_joinstyle='miter')
l3, l4 = ax.plot(x, x**3, '-.o', x, np.exp(-x), 's-b')


# Set legend
leg = plt.legend((l2, l3, l4), ('quadratic', 'cubic', 'exponential'), loc='upper right', shadow=True, title="Legend", fancybox=True)
leg.get_title().set_color("red")

ax.set_title('Legend Demo')
ax.set_xlabel('x label')
ax.set_ylabel('y label')

plt.savefig('set_legend.pdf')
plt.show()
