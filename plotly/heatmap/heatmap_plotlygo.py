import plotly.figure_factory as ff
import numpy as np
import plotly

disease = ['Amebiasis', 'Dengue Virus Infection', 'Salmonellosis', 'Campylobacteriosis']
county = ['Alameda', 'Los Angeles', 'San Diego', 'San Francisco']
cases = np.array([[12, 75, 62, 52],
                  [5, 36, 8, 7],
                  [272, 1228, 534, 174],
                  [391, 1573, 841, 389]])

fig = ff.create_annotated_heatmap(z=cases, x=disease, y=county, annotation_text=cases, colorscale='Viridis')

fig.update_layout(title='Disease by California County')
plotly.offline.plot(fig, filename='heatmap_plotlygo_ca_disaese.html')
fig.show()
