# Boxplot of Car sale in California from 08/2018 - 08/2019
import pandas as pd
import matplotlib.pyplot as plt
font_param = {'size': 14, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

# plt.style.use('seaborn')

# Prepare data
ca_car_sale = pd.read_csv('multiTimeline.csv', header=1)
print(ca_car_sale.head())
print(ca_car_sale.tail())


# Plot data
flier_props = dict(markerfacecolor='b', marker='d')
fig1, ax = plt.subplots(1, 2, figsize=(10,5))

# rectangular box plot
box_plot1 = ax[0].boxplot([ca_car_sale['hybrid car sale: (California)'],
                           ca_car_sale['electric car sale: (California)']],
                          labels=['Hybrid Car', 'Electric Car'],
                          flierprops=flier_props, widths=0.35,
                          patch_artist=True)

# notch shape box plot
box_plot2 = ax[1].boxplot([ca_car_sale['hybrid car sale: (California)'],
                           ca_car_sale['electric car sale: (California)']],
                          labels=['Hybrid Car', 'Electric Car'],
                          flierprops=flier_props, widths=0.35,
                          patch_artist=True, notch=True)

ax[0].set_title('California Car Sale 08/2018-08/2019', font_param)
ax[1].set_title('California Car Sale 08/2018-08/2019', font_param)

# fill with colors
colors = ['lightgreen', 'lightblue']
for bplot in (box_plot1, box_plot2):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

# Set y-label
for ax in ax:
    ax.set_ylabel('Sales Count', size=10, fontweight='semibold')


plt.tight_layout()
plt.savefig('boxplot_ca_car_sale.pdf')
plt.show()
