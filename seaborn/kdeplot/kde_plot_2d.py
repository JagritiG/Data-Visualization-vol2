# 2D Density plot using kdetplot()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

sns.set(style="white", palette="dark", color_codes=True)

# Load tips data from file into pandas DataFrame
tips = pd.read_csv('tips.csv')

# Plot 2D kernel density plot
x = tips["total_bill"]
y = tips["tip"]
data = tips

# If cbar=True, draw a bivariate KDE plot, add a colorbar
# shade=True, shade in the area under the KDE curve
kde = sns.kdeplot(x, y, cbar=True, shade=True)
kde.set_title('2D Density plot of Total Bill and Tip',
              font_param)
kde.set_xlabel('Total Bill')
kde.set_ylabel('Tip')

plt.tight_layout()

# Save and show figure
fig = kde.get_figure()
fig.savefig('kde_2d_totalbill_tip.pdf')
plt.show()


