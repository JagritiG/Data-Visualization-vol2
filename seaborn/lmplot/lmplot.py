# Scatter plot using lmplot()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

sns.set(color_codes=True)

# Load Data
col_names = ['Sepal_length', 'Sepal_width', 'Petal_length', 'Petal_width', 'Species']
iris = pd.read_csv('iris.csv', names=col_names)


# Draw lmplot of iris sepal comparison
x = 'Sepal_length'
y = 'Sepal_width'
hue = 'Species'
data = iris

# Plot scatter plot and also fit a regression line
scatter = sns.lmplot(x, y, data, hue=hue,
                     truncate=True, height=4,
                     aspect=1.5, legend=False)
scatter.set_axis_labels("Sepal length (mm)", "Sepal width (mm)")
ax = plt.gca()
ax.set_title('Sepal length vs Sepal Width', font_param)

ax.legend(loc='upper right', fontsize='x-small', title='Species', title_fontsize=10, fancybox=True)
plt.tight_layout()

# Save and show figure
scatter.savefig('lmplot_iris.pdf')
plt.show()
