# Errorbar with bar plots
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

plt.style.use('bmh')

# Prepare data
ca_car_sale = pd.read_csv('multiTimeline.csv', header=1)
print(ca_car_sale.head())
print(ca_car_sale.tail())

# Calculate the average sale
hybrid_car_mean = np.mean(ca_car_sale['hybrid car sale: (California)'])
electric_car_mean = np.mean(ca_car_sale['electric car sale: (California)'])
print(hybrid_car_mean)
print(electric_car_mean)

# Calculate the standard deviation
hybrid_car_std = np.std(ca_car_sale['hybrid car sale: (California)'])
electric_car_std = np.std(ca_car_sale['electric car sale: (California)'])
print(hybrid_car_std)
print(electric_car_std)

# Define labels, positions, bar heights and error bar heights
labels = ['hybrid car', 'electric car']
x_pos = np.arange(len(labels))
bar_hight = [hybrid_car_mean, electric_car_mean]
error_bar_hight = [hybrid_car_std, electric_car_std]

# Plot data
fig, ax = plt.subplots()
ax.bar(x_pos, bar_hight, yerr=error_bar_hight, align='center', alpha=0.5, ecolor='black', capsize=10)

ax.set_ylabel('Sales', size=10, fontweight='semibold' )
ax.set_xticks(x_pos)
ax.set_xticklabels(labels)
ax.set_title('California Car Sales 08/2018-08/2019', font_param)

# Save the figure and show
plt.tight_layout()
plt.savefig('bar_plot_with_error_bar_carsale.pdf')
plt.show()
