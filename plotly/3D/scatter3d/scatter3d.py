import plotly.express as px
import plotly.graph_objects as go
import plotly
import pandas as pd


col_names = ['Sepal_length', 'Sepal_width', 'Petal_length', 'Petal_width', 'Species']
iris = pd.read_csv('iris.csv', names=col_names)

fig = px.scatter_3d(iris, x='Sepal_length',
                    y='Sepal_width', z='Petal_width',
                    color='Petal_length', symbol='Species',
                    color_continuous_scale=px.colors.sequential.Plasma)


# tight layout
fig.update_layout(legend=go.layout.Legend(
        x=0,
        y=1,
        traceorder="normal",
        font=dict(
            family="sans-serif",
            size=12,
            color="black"
        ),
        bgcolor="white",
        bordercolor="Blue",
        borderwidth=2))

plotly.offline.plot(fig, filename='scatter3d_iris_px.html')
fig.show()
