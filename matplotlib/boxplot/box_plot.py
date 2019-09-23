# Boxplot of 'Tips' data
import pandas as pd
import matplotlib.pyplot as plt
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}


# Prepare data
tips = pd.read_csv('tips.csv',)
print(tips.head())

flier_props = dict(markerfacecolor='b', marker='d')
fig1, ax = plt.subplots()
ax.boxplot([tips[tips['sex'] == 'Female']['tip'],
            tips[tips['sex'] == 'Male']['tip']], labels=['Female', 'Male'], flierprops=flier_props, widths=0.35,
                 patch_artist=True, boxprops=dict(facecolor="lightgray"))

ax.set_xlabel('Sex', fontsize=10, fontweight='semibold')
ax.set_ylabel('Tips', fontsize=10, fontweight='semibold')
ax.set_title('Tips by Sex', font_param)

plt.tight_layout()
plt.savefig('boxplot_tips.pdf')
plt.show()
