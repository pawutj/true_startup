import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import altair as alt
from vega_datasets import data

import datetime
# section2 ###########################################

df = pd.DataFrame({
    'xval': ["1", "1", "2-3", "2-3", "4-5", "4-5", "6-10", "6-10", "11+", "11+"],
    'group': [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
    "value": [5000, 8000, 500, 3000, 100, 1000, 60, 800, 30, 300]
})

c = alt.Chart(df).mark_bar().encode(
    x=alt.X('group:O', axis=alt.Axis(title=None, labels=False, ticks=False)),
    y=alt.Y('value:Q', axis=alt.Axis(grid=False)),
    color='group:N',
    column=alt.Column(
        'xval:N',
        sort=["1", "2-3", "4-5", "6-10", "11+"],
        header=alt.Header(title=None, labelOrient='bottom')
    )
).configure_view(
    stroke='transparent'
)

st.altair_chart(c)
############################################################## Datetime #
d = st.date_input(
    "When's your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)
# 3
st.button("Re-run")
