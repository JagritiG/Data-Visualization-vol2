# Example of barplot using titanic data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

sns.set(style="whitegrid", color_codes=True)

# Load the example Titanic dataset
titanic = pd.read_csv("titanic.csv")


# Draw a nested barplot to show survival for class and sex
x = "Pclass"
y = "Survived"
hue = "Sex"
data = titanic

g = sns.catplot(x, y, hue, data,
                height=5, kind="bar",
                aspect=1, palette="bright",
                hue_order=['female', 'male'])
g.despine(left=True)
g.set_ylabels("Survival Probability")
plt.title('Titanic Survival Probability', font_param, pad=0.4)

g.savefig('bar_titanic.pdf')
plt.show()

