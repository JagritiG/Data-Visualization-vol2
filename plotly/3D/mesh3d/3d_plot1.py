import plotly.graph_objects as go
import numpy as np
import plotly

# Define random surface
N = 50
fig = go.Figure()
fig.add_trace(go.Mesh3d(x=(60*np.random.randn(N)),
                   y=(25*np.random.randn(N)),
                   z=(40*np.random.randn(N)),
                   opacity=0.8,
                   color='yellow'
                  ))
fig.add_trace(go.Mesh3d(x=(70*np.random.randn(N)),
                   y=(55*np.random.randn(N)),
                   z=(30*np.random.randn(N)),
                   opacity=0.4,
                   color='purple'
                  ))

fig.update_layout(scene = dict(
                    xaxis_title='X AXIS TITLE',
                    yaxis_title='Y AXIS TITLE',
                    zaxis_title='Z AXIS TITLE'),
                    width=700,
                    margin=dict(r=20, b=10, l=10, t=10))

plotly.offline.plot(fig, filename='mash3d.html')
fig.show()
