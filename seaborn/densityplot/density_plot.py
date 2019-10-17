import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
font_param = {'size': 12, 'fontweight': 'semibold',
              'family': 'serif', 'style': 'normal'}

sns.set(style="white", palette="deep", color_codes=True)

# Load nba data from file into pandas DataFrame
nba = pd.read_csv('processed_nba.csv')
a = nba['Weight']

# Plot histogram and kernel density estimation (kde) with rugplot using distplot()
kde_kws={"color": "k", "lw": 2, "label": "KDE"}
hist_kws={"histtype": "stepfilled", "linewidth": 3,
          "alpha": 1, "color": "lightblue"}

dist = sns.distplot(a, rug=True, rug_kws={"color": "r"},
                    kde_kws=kde_kws, hist_kws=hist_kws)


dist.set_title('Weight Distribution of NBA Players', font_param)
dist.set_xlabel('Weight in lb')
dist.set_ylabel('Freguency')

plt.tight_layout()

# Save and show figure
fig = dist.get_figure()
fig.savefig('hdr_nba_weigth.png')
plt.show()

# Plot histogram and kernel density estimation
hd = sns.distplot(a, bins=15, color='royalblue')
hd.set_title('Weight Distribution of NBA Players', font_param)
hd.set_xlabel('Weight in lb')
hd.set_ylabel('Freguency')

plt.tight_layout()

# Save and show figure
fig = hd.get_figure()
fig.savefig('hd_nba_weigth.png')
plt.show()

# Plot only histogram
hist = sns.distplot(a, bins=15, kde=False, color='royalblue')
hist.set_title('Weight Distribution of NBA Players', font_param)
hist.set_xlabel('Weight in lb')
hist.set_ylabel('Freguency')

plt.tight_layout()

# Save and show figure
fig = hist.get_figure()
fig.savefig('hist_nba_weigth.png')
plt.show()

# plot kernel density estimate
kde = sns.distplot(a, hist=False, color='royalblue')
kde.set_title('Weight Distribution of NBA Players', font_param)
kde.set_xlabel('Weight in lb')
kde.set_ylabel('Freguency')

plt.tight_layout()

# Save and show figure
fig = kde.get_figure()
fig.savefig('kde_nba_weigth.png')
plt.show()

# plot kernel density with filled area
kde = sns.distplot(a, hist=False, color='royalblue',
                   kde_kws={"shade": True})
kde.set_title('Weight Distribution of NBA Players', font_param)
kde.set_xlabel('Weight in lb')
kde.set_ylabel('Freguency')

plt.tight_layout()

# Save and show figure
fig = kde.get_figure()
fig.savefig('kde_filled_nba_weigth.png')
plt.show()

# Plot histogram with rug
hr = sns.distplot(a, bins=15, kde=False, rug=True,
                  color='royalblue', rug_kws={"color": "r"})
hr.set_title('Weight Distribution of NBA Players', font_param)
hr.set_xlabel('Weight in lb')
hr.set_ylabel('Freguency')

plt.tight_layout()

# Save and show figure
fig = hr.get_figure()
fig.savefig('hr_nba_weigth.png')
plt.show()

# plot kernel density with rug
kder = sns.distplot(a, bins=15, hist=False, rug=True,
                    color='royalblue', rug_kws={"color": "r"})
kder.set_title('Weight Distribution of NBA Players', font_param)
kder.set_xlabel('Weight in lb')
kder.set_ylabel('Freguency')

plt.tight_layout()

# Save and show figure
fig = kder.get_figure()
fig.savefig('kder_nba_weigth.png')
plt.show()
