import streamlit as st
import pandas as pd
st.title("Streamlit Text Input")

name=st.text_input("Enter your name:")
age=st.slider("Select your age",0,100,25)

st.write(f"Your age is {age}")
options=['python','java','c++','js']
choice=st.selectbox("Chose your favorite language:",options)
st.write(f"You selected {choice}")
if name:
    st.write(f"Hello,{name}")

data={
    "Name":["Rajib","ajim","jony"],
    "Age":[21,22,23],
    "City":["Salar","Pilkhundi","talibpur"]
}
df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)
uploaded_file=st.file_uploader('Chose a csv file',type='csv')    

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)