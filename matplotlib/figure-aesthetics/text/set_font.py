# The size, style, fontweight, family, and variant parameters can be set under font.
# They can be set as keyword arguments directly in a text command.
# Also they can be stored and passed as a dictionary with keys of parameter names in strings
# and their corresponding values.

import matplotlib.pyplot as plt
import numpy as np
font_param = {'size': 16, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

x = np.linspace(0, 2, 100)

fig, ax = plt.subplots()
ax.set_title('Simple plot', font_param)
ax.set_xlabel('x label', size='14', fontweight='medium', style='normal', family='serif')
ax.set_ylabel('y label', size='14', fontweight='medium', style='normal', family='serif')
ax.plot(x, x, label='linear', color='C4', linestyle=':', lw=2)
ax.plot(x, x**2, label='quadratic', color='C2', linestyle='--', lw=2)
ax.plot(x, x**3, label='cubic', color='C3', linestyle='-.', lw=2)


plt.legend()
plt.savefig('set_text_font.pdf')
plt.show()
