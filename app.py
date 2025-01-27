import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Sample data generation (same as before)
n = 20
bid_vol_excess = np.linspace(0, 600, n)
lines_cm = np.random.randint(20, 100, n)
lines_cu = np.random.randint(20, 100, n)
weights = np.random.randint(100, 1000, n)

data = {
    'Bid Vol Excess': bid_vol_excess,
    'Lines CM (One Way)': lines_cm,
    'Lines CU (One Way)': lines_cu,
    'Weight': weights
}
df = pd.DataFrame(data)

# Streamlit app
st.title("GLM Model Replication")

# Metric selection
selected_metrics = st.multiselect(
    "Metric Selection",
    ['Lines CM (One Way)', 'Lines CU (One Way)'],
    default=['Lines CM (One Way)']
)

# Rescale selection
rescale = st.selectbox(
    "Rescale Switch",
    ["No Rescaling", "Rescale to Min-Max", "Rescale to Z-Score"]
)

# Plot function
def plot_data(selected_metrics, rescale):
    fig = go.Figure()

    # Bar chart for the selected metric
    for metric in selected_metrics:
        fig.add_trace(go.Bar(
            x=df['Bid Vol Excess'],
            y=df[metric],
            name=metric,
            marker_color='yellow',
            yaxis='y1'
        ))

    # Line chart for weight
    fig.add_trace(go.Scatter(
        x=df['Bid Vol Excess'],
        y=df['Weight'],
        mode='lines+markers',
        name='Weight',
        line=dict(color='orange', width=2),
        marker=dict(size=8),
        yaxis='y2'
    ))

    # Update layout
    fig.update_layout(
        xaxis_title="Bid Vol Excess",
        yaxis=dict(title='Response', side='left', titlefont=dict(color='black'), tickfont=dict(color='black')),
        yaxis2=dict(title='Weight', overlaying='y', side='right', titlefont=dict(color='black'), tickfont=dict(color='black')),
        legend=dict(x=0, y=1),
        template='plotly_white'
    )

    return fig

# Display the plot
if selected_metrics:
    st.plotly_chart(plot_data(selected_metrics, rescale))
else:
    st.warning("Please select at least one metric.")
