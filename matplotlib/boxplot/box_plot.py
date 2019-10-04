# Boxplot of 'Tips' data
import pandas as pd
import matplotlib.pyplot as plt
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}


# Prepare data
tips = pd.read_csv('tips.csv',)
print(tips.head())

# Plot data
x = [tips[tips['sex'] == 'Female']['tip'],
            tips[tips['sex'] == 'Male']['tip']]
label = ['Female', 'Male']
box_props = dict(facecolor="lightblue")
median_props = dict(color="coral", lw=1.5)
flier_props = dict(markerfacecolor='b', marker='d')

fig1, ax = plt.subplots()
ax.boxplot(x, labels=label, flierprops=flier_props,
           widths=0.35, patch_artist=True,
           boxprops=box_props,
           medianprops=median_props)


ax.set_xlabel('Sex', fontsize=10)
ax.set_ylabel('Tips', fontsize=10)
ax.tick_params(axis='both', direction='out',
               length=2, width=0.5, )
ax.set_title('Tips by Sex', font_param)

plt.tight_layout()
plt.savefig('boxplot_tips.pdf')
plt.show()
