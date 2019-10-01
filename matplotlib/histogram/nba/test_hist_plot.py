import pandas as pd
import matplotlib.pyplot as plt
from hist_func import plot_hist

# Load nba data from file into pandas DataFrame
nba = pd.read_csv('processed_nba.csv',)

# Call function plot_hist()
plot_hist(nba['Weight'], 'Histogram of Weight', 'Weight in lb', 'Frequency', 'test_plot_hist.pdf')

# Show plot
plt.show()
