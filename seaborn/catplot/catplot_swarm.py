# Example of swarmplot using tips dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

sns.set(style="whitegrid", color_codes=True)

# Load the example dataset
tips = pd.read_csv("tips.csv")


# Draw a swarm plot of total bill vs day
x = "day"
y = "total_bill"
hue = "sex"
order=['Thur', 'Fri', 'Sat', 'Sun']
data = tips

g = sns.catplot(x=x, y=y, data=data, kind='swarm', hue=hue, order=order)
g.despine(left=True)
plt.title('Swarmplot of total bill vs day', font_param, pad=0.4)

g.savefig('swarm_tips.pdf')
plt.show()

