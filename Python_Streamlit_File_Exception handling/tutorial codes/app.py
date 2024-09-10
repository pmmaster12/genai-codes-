import streamlit as st
import pandas as pd
import numpy as np

# 1-title of application
st.title("hello streamlit")

# display simple text
st.write("this is simple")

df=pd.DataFrame({'first col':[1,2,3,4],'second col':[5,6,7,8]})

#display data frame
st.write("here is simple data frame")
st.write(df)
#line chart
chart_Data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_Data)


