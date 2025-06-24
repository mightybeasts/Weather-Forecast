# visualize.py
import pandas as pd
import plotly.express as px



def plot_temperature_chart(df):
    df['time'] = pd.to_datetime(df['time'])
    fig = px.line(
        df,
        x='time',
        y='temperature',
        title='Hourly Temperature Forecast',
        markers=True,
        labels={"temperature": "Temp (°C)", "time": "Time"},
        line_shape="spline",
    )
    fig.update_traces(line_color='deepskyblue')
    fig.update_layout(template='plotly_dark')
    return fig


