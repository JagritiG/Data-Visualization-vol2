# Violin plot
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}


# Load Data
col_names = ['Sepal_length', 'Sepal_width', 'Petal_length', 'Petal_width', 'Species']
iris = pd.read_csv('iris.csv', names=col_names)

x = iris['Species']
y = iris['Sepal_length']
hue = iris['Species']
data = iris

# Draw violinplot to show sepal length comparison
sepal_length = sns.violinplot(x, y, data=data, hue=hue)
sepal_length.set_title("Sepal Length Comparison", font_param)
sepal_length.set_xlabel("Species", size=10, fontweight='semibold')
sepal_length.set_ylabel("Sepal Length", size=10, fontweight='semibold')

plt.legend(loc='upper left', fontsize='small', title='Species', title_fontsize=10, fancybox=True)
plt.tight_layout()
fig = sepal_length.get_figure()
fig.savefig('iris_sepal_comparison.pdf')
plt.show()




