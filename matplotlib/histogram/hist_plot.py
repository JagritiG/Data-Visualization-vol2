import pandas as pd
import matplotlib.pyplot as plt


# Function for plotting histogram
def plot_hist(data, title, x_label, y_label, filename):
    font_param = {'size': 12, 'fontweight': 'semibold',
                  'family': 'serif', 'style': 'normal'}

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.hist(data, 10, density=1)
    # these are matplotlib.patch.Patch properties
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    ax.set_title(title, font_param)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    fig.tight_layout()
    plt.savefig(filename)


if __name__ == "__main__":
    # Load nba data from file into pandas DataFrame
    nba = pd.read_csv('processed_nba.csv',)
    # Call function plot_hist()
    plot_hist(nba['Weight'], 'Histogram of Weight', 'Weight in lb', 'Frequency', '../hist_plot.pdf')
    # Show plot
    plt.show()



