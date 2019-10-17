# Example of violin plot using iris dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

sns.set(style="whitegrid", color_codes=True)

# Load Data
col_names = ['Sepal_length', 'Sepal_width', 'Petal_length', 'Petal_width', 'Species']
iris = pd.read_csv('iris.csv', names=col_names)


# Draw a  violinplot of iris sepal comparison
x = 'Species'
y = 'Sepal_length'
data = iris

g = sns.catplot(x=x, y=y, data=data, kind='violin')
g.despine(left=True)
plt.title('Violin plot of iris sepal comparison', font_param, pad=0.4)

g.savefig('violin_iris_sepal_comparison.pdf')
plt.show()
