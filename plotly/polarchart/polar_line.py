import plotly.express as px
import plotly

wind = px.data.wind()
fig = px.line_polar(wind, r="frequency",
                    theta="direction", color="strength", line_close=True,
                    color_discrete_sequence=px.colors.sequential.Plasma,
                    template="plotly_white",)

fig.update_layout(
  title="Wind Strength"
)

fig.update_traces(fill='toself')

plotly.offline.plot(fig, filename='polarplot_px.html')
fig.show()
