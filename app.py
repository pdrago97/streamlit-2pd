import streamlit as st
import plotly.graph_objects as go
import math

st.title('Distance Between Two Points Calculator')

# Get input values
x1 = st.number_input('Enter x coordinate of first point:')
y1 = st.number_input('Enter y coordinate of first point:')
z1 = st.number_input('Enter z coordinate of first point:')
x2 = st.number_input('Enter x coordinate of second point:')
y2 = st.number_input('Enter y coordinate of second point:')
z2 = st.number_input('Enter z coordinate of second point:')

# Calculate distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

# Plot points and line connecting them
fig = go.Figure(data=[go.Scatter3d(x=[x1, x2], y=[y1, y2], z=[z1, z2],
                         mode='lines+markers')])
st.plotly_chart(fig)

# Display result
st.write(f'The distance between the two points is {distance:.2f}')