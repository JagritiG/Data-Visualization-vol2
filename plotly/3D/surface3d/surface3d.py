import plotly.graph_objects as go
import pandas as pd
import plotly

# Read data from a csv
temp = pd.read_csv('city_temp.csv')
print(temp.values)


fig = go.Figure(data=[go.Surface(z=temp.values)])

fig.update_layout(title='City Temperature for the Month January', autosize=True,
                  width=500, height=500,
                  scene={"xaxis": {'title': "xaxis_title",
                                   "tickfont": {"size": 10}, 'type': "linear"},
                         "yaxis": {'title': "yaxis_title",
                                   "tickfont": {"size": 10}, 'tickangle': 1},
                         "zaxis": {'title': "zaxis_title",
                                   "tickfont": {"size": 10}}},

                  margin=dict(l=65, r=50, b=65, t=90),
                  scene_camera_eye=dict(x=2, y=1, z=3))

plotly.offline.plot(fig, filename='surface3d_temp_go.html')
fig.show()
