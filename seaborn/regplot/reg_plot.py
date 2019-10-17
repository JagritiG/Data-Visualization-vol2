# Example of regplot()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

sns.set(color_codes=True)

# Load tips data from file into pandas DataFrame
tips = pd.read_csv('tips.csv')

# Plot 2D kernel density plot
x = "total_bill"
y = "tip"
data = tips

# Plot scatter plot and also fit a regression line
scatter = sns.regplot(x, y, data=data, color="seagreen")
ax = plt.gca()
ax.set_title('Regplot of total bill vs tips', font_param)

plt.tight_layout()

# Save and show figure
plt.savefig('regplot_totalbill_tip.pdf')
plt.show()
