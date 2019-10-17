# Pairwise relationship between numeric data using pairplot()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(color_codes=True)

# Load tips data from file into pandas DataFrame
# Load Data
col_names = ['Sepal_length', 'Sepal_width', 'Petal_length', 'Petal_width', 'Species']
iris = pd.read_csv('iris.csv', names=col_names)

# Draw pairwise plot
data = iris
hue = 'Species'
pair_plot= sns.pairplot(data, hue=hue)
pair_plot.fig.suptitle("Iris Species Comparison", fontsize=12, fontweight='semibold', y=1)

pair_plot.savefig("pairplot_iris.pdf")
plt.show()
