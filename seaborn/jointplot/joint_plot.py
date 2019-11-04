# Example of jointplot
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(color_codes=True)

# Load tips data from file into pandas DataFrame
tips = pd.read_csv('tips.csv')

# Regplot with a univariate plot on each axis using jointplot()
x = tips["total_bill"]
y = tips["tip"]
data = tips

scatter = sns.jointplot(x, y, data=data, kind='reg',
                        height=5, ratio=5, space=4,
                        color='royalblue')
scatter.set_axis_labels("Total Bill", "Tip")

# add a title, set font size, and move the text above the total axes
scatter.fig.suptitle("Jointplot of Total Bill and Tip",
                     fontsize=12, fontweight='semibold', y=1)
plt.tight_layout()
scatter.savefig("jointplot_totalbill_tip.pdf")
plt.show()
