import streamlit as st
import pandas as pd

import matplotlib.pyplot as fig

df = pd.DataFrame(data={'Name':['Jessica','John','Alex'],
    'Score 1':[77,56,87],'Score 2':[76,97,82]}
)
df = df.set_index('Name')
df.plot(kind='bar',stacked=False,xlabel='Name',ylabel='Score')
st.pyplot(fig)