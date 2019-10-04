# Heatmap using California Disease data
import numpy as np
import matplotlib.pyplot as plt
from helpFunc.heatmap_help import Heatmap
font_param = {'size': 12, 'fontweight': 'semibold',
                  'family': 'serif', 'style': 'normal'}


# Source: Infectious Diseases by County, Year and Sex , 2014
# url: https://data.chhs.ca.gov/dataset/infectious-disease/resource/75019f89-b349-4d5e-825d-8b5960fc028c

# ToDo: Prepare data
disease = ['Amebiasis', 'Dengue Virus Infection', 'Salmonellosis', 'Campylobacteriosis']
county = ['Alameda', 'Los Angeles', 'San Diego', 'San Francisco']
cases = np.array([[12, 75, 62, 52],
                  [5, 36, 8, 7],
                  [272, 1228, 534, 174],
                  [391, 1573, 841, 389]])

# Plot data
data = cases
row_labels = disease
col_labels = county
fig, ax = plt.subplots()

im, cbar = Heatmap.heatmap(data, row_labels, col_labels, ax=ax,
                   cmap="rainbow", cbarlabel="Number of Cases")
texts = Heatmap.annotate_heatmap(im, valfmt="{x:.0f}")

ax.set_title("Infectious Diseases by County\nCalifornia - 2014", font_param)
plt.tight_layout()
plt.savefig('heatmap_disease.pdf')
plt.show()
