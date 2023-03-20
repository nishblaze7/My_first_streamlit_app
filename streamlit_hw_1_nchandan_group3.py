import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd

st.header('Homework 1')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)

import random
x_limit = 100
x_axis = np.arange(0,x_limit,1)
y_data = [random.random() for value in x_axis]
df = pd.DataFrame({'Input': x_axis,
                     'Output': y_data})
st.write(df)

st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)

scatter = alt.Chart(df).mark_point(color= 'Red').encode(x='Input',y='Output')

st.altair_chart(scatter, use_container_width=True)


st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)
st.markdown(
      "Change 1: Changed x and y axis names, change 2: changed color = Red, Change 3 & 4: Adding 2 different themes to the scatterplot"
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    st.altair_chart(scatter, theme="streamlit", use_container_width=True)
with tab2:
        st.altair_chart(scatter, theme=None, use_container_width=True)

st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)

import altair as alt
from vega_datasets import data

source = data.wheat()

bar = alt.Chart(source).mark_bar().encode(
    x='year:O',
    y='wheat:Q'
)

line = alt.Chart(source).mark_line(color='red').transform_window(
    # The field to average
    rolling_mean='mean(wheat)',
    # The number of values before and after the current value to include.
    frame=[-9, 0]
).encode(
    x='year:O',
    y='rolling_mean:Q'
)

(bar + line).properties(width=600)

st.altair_chart(bar + line)


