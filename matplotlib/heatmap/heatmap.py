# Heatmap using California Disease data
import numpy as np
import matplotlib.pyplot as plt
from helpFunc.heatmap_help import Heatmap


# Source: Infectious Diseases by County, Year and Sex
# url: https://data.chhs.ca.gov/dataset/infectious-disease/resource/75019f89-b349-4d5e-825d-8b5960fc028c

# ToDo: Prepare data
disease = ['Amebiasis', 'Dengue Virus Infection', 'Zika Virus Infection']
county = ['ALAMEDA', 'LOS ANGELES', 'SAN DIEGO']
cases = np.array([[67.0, 76.0, 10.0],
                  [7.0, 28.0,  9.0],
                  [7.0, 17.0,  8.0]])

# Plot data
fig, ax = plt.subplots()

im, cbar = Heatmap.heatmap(cases, disease, county, ax=ax,
                   cmap="Greens", cbarlabel="Number of Cases")
texts = Heatmap.annotate_heatmap(im, valfmt="{x:.0f}")

ax.set_title("No of Disease CA County-wise for 2018")
plt.tight_layout()
plt.savefig('heatmap.pdf')
plt.show()
