# Set linestyle or ls ('-', '--', '-.', ':', ",...), linewidth or lw, capstyle for dashed and solid lines ('butt', 'round', 'projecting'),
# join style for dashed and solid lines ('miter', 'round', 'bevel').
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)

fig, ax = plt.subplots()
ax.set_title('Simple plot')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.plot(x, x, label='linear', color='C4', linestyle=':', linewidth=3, dash_capstyle='round', dash_joinstyle='round')
ax.plot(x, x**2, label='quadratic', c='C2', ls='--', lw=2.5, dash_capstyle='projecting', dash_joinstyle='miter')
ax.plot(x, x**3, label='cubic', c='C3', ls='-', lw=2, solid_capstyle='butt', solid_joinstyle='bevel')


plt.legend()
plt.savefig('set_line.pdf')
plt.show()
