import plotly.graph_objects as go
import plotly

fig = go.Figure(go.Waterfall(
    name="20", orientation="v",
    measure=["relative", "relative", "total", "relative", "relative", "total"],
    x=["Sales", "Consulting", "Net revenue", "Purchases", "Other expenses", "Profit before tax"],
    textposition="outside",
    text=["+60", "+80", "", "-40", "-20", "Total"],
    y=[60, 80, 0, -40, -20, 0],
    connector={"line":{"color":"rgb(63, 63, 63)"}},
))

fig.update_layout(
        title="Profit and loss statement 2018",
        showlegend=True
)

plotly.offline.plot(fig, filename='waterfall_plotlygo.html')
fig.show()
