import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)

# RGB tuple:
fig, ax = plt.subplots(facecolor=(0.001, 0.002, 0.004, 0.003))
# hex string:
ax.set_facecolor('#eafff5')
# gray level string:
ax.set_title('Simple plot', fontweight='bold', color='0.04')
# single letter color string
ax.set_xlabel('x label', color='b', fontweight='semibold')
# a named color:
ax.set_ylabel('y label', color='blue', fontweight='semibold')
# Cn notation:
ax.plot(x, x, label='linear', color='C4', linestyle=':', lw=2)
ax.plot(x, x**2, label='quadratic', color='C2', linestyle='--', lw=2)
ax.plot(x, x**3, label='cubic', color='C3', linestyle='-.', lw=2)
# tab notation:
ax.tick_params(labelcolor='tab:gray')

plt.legend()
plt.savefig('set_color.pdf')
plt.show()
