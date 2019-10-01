# Scatter plot using Iris dataset
import pandas as pd
import matplotlib.pyplot as plt


# Function for plotting histogram
def plot_scatter(dataset, x, y, label, title, filename):
    font_param = {'size': 12, 'fontweight': 'semibold',
                  'family': 'serif', 'style': 'normal'}

    dataset.plot(x, y, kind="scatter", label=label, color='b')

    plt.title(title, font_param)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)


if __name__ == "__main__":
    # Load nba data from file into pandas DataFrame
    setosa = pd.read_csv('setosa.csv')
    # Call function plot_scatter()
    plot_scatter(setosa, 'Sepal_length', 'Sepal_width', 'Setosa', 'Sepal Comparison', 'plot_scatter.pdf')
    # Show plot
    plt.show()


