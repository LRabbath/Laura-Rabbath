import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Bar(
    x=['Scénario 0', 'Scénario 1a', 'Scénario 1b','Scénario 2a', 'Scénario 2b', 'Scénario 3a','Scénario 3b'],
    y=[1696.28, 2347.17, 346.25, 0.00, 0.00, 0.00, 0.00],
    name='Electricité'
)
trace2 = go.Bar(
    x=['Scénario 0', 'Scénario 1a', 'Scénario 1b','Scénario 2a', 'Scénario 2b', 'Scénario 3a','Scénario 3b'],
    y=[725.97, 564.43, 568.36, 0.00, 0.00, 0.00, 0.00],
    name='Chaleur'
)

data = [trace1, trace2]
layout = go.Layout(
    barmode='stack'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='stacked-bar')
