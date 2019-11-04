import plotly
import plotly.graph_objects as go

esg_performance = ['Environmental','Social','Governance']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=[4.5, 3, 3.05],
      theta=esg_performance,
      fill='toself',
      name='AAPL'
))
fig.add_trace(go.Scatterpolar(
      r=[3.39, 3.215, 3.2],
      theta=esg_performance,
      fill='toself',
      name='Sector'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 5]
    )),
  title="AAPL ESG Performance vs 57 Peer Companies",
  showlegend=True
)

plotly.offline.plot(fig, filename='radarchart_go_apple.html')
fig.show()
