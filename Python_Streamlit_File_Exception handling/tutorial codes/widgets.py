import streamlit as st
import pandas as pd
st.title('streamlit text input')
name=st.text_input('enter your name')
age=st.slider("select your age:",0,100,20)
st.write(f'your age is{age}')
if name:
    st.write(f"hello {name}")

options=['python','c++','c#','java','php']
choices=st.selectbox("choose your language for code:",options)
st.write(f"you choose {choices} language")

upload_file=st.file_uploader("choose a text file",type="txt")

if upload_file:
    content=upload_file.read()
    st.write(content)
else:

    st.write('pls upload a text file')



