# Scatter plot using Iris dataset
import pandas as pd
import matplotlib.pyplot as plt
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

# Prepare data for plotting
# load iris dataset from file in Pandas Dataframe
col_names = ['Sepal_length', 'Sepal_width', 'Petal_length', 'Petal_width', 'Species']
iris = pd.read_csv('iris.csv', names=col_names)

# Print first 5 and last 5 rows from DataFrame to check if data is correctly loaded
print(iris.head())
print(iris.tail())

# Find out unique class of iris flower
print(iris['Species'].unique())

# Find out no of rows for each Species
print(iris.groupby('Species').size())

# Create 3 DataFrame for each Species
setosa = iris[iris['Species'] == 'Iris-setosa']
versicolor = iris[iris['Species'] == 'Iris-versicolor']
virginica = iris[iris['Species'] == 'Iris-virginica']

print(setosa.describe())
print(versicolor.describe())
print(virginica.describe())

print(iris.describe())

# Plotting Petal length vs Petal width and Sepal length vs Sepal width
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
iris.plot(x="Sepal_length", y="Sepal_width", kind="scatter",ax=ax[0], label="Sepal", color='b')
iris.plot(x="Petal_length", y="Petal_width", kind="scatter",ax=ax[1], label="Petal", color='g',)

ax[0].set_title('Sepal Comparison', font_param)
ax[1].set_title('Petal Comparison', font_param)
ax[0].legend()
ax[1].legend()

plt.tight_layout()
plt.savefig('scatter_plot.pdf')

# For each Species ,let's check what is petal and sepal distribution
fig, ax = plt.subplots(1,2,figsize=(10, 5))
setosa.plot(x="Sepal_length", y="Sepal_width",
            kind="scatter", ax=ax[0],
            label='setosa', color='r')
versicolor.plot(x="Sepal_length", y="Sepal_width",
                kind="scatter",ax=ax[0],
                label='versicolor', color='b')
virginica.plot(x="Sepal_length", y="Sepal_width",
               kind="scatter", ax=ax[0],
               label='virginica', color='g')

setosa.plot(x="Petal_length", y="Petal_width",
            kind="scatter",ax=ax[1],
            label='setosa',color='r')
versicolor.plot(x="Petal_length", y="Petal_width",
                kind="scatter", ax=ax[1],
                label='versicolor', color='b')
virginica.plot(x="Petal_length", y="Petal_width",
               kind="scatter", ax=ax[1],
               label='virginica', color='g')

ax[0].set_title('Sepal Comparison', font_param)
ax[1].set_title('Petal Comparison', font_param)
ax[0].legend()
ax[1].legend()

plt.tight_layout()
plt.savefig('petal_and_sepal_distibutuon_for_each_species.pdf')
plt.show()

# Observation:
# Satosa   - satosa Petal are relatively smaller than rest of species.
# satosa petal < versicolor petal < virginica petal
# Satosa sepal are smallest in length and largest in Width than other species
