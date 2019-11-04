import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

sns.set(style="white", palette="deep", color_codes=True)

# Load nba data from file into pandas DataFrame
nba = pd.read_csv('processed_nba.csv')
x = nba['Weight']

kde = sns.kdeplot(x, cbar=True, shade=True)
kde.set_title('Weight Distribution of NBA Players',
              font_param)
kde.set_xlabel('Weight in lb')
kde.set_ylabel('Freguency')

plt.tight_layout()

# Save and show figure
fig = kde.get_figure()
fig.savefig('hdr_nba_weigth.pdf')
plt.show()
