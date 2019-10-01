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

# Save setosa dataframe into csv file
setosa.to_csv('setosa.csv')
setosa.to_csv('versicolor.csv')
setosa.to_csv('virginica.csv')
