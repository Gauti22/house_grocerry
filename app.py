import streamlit as st
from src.grocerry import data_read, processing
from src.schedule import processing1, processing2 , processing3
import pandas as pd

st.title('House cooking and grocerry status')

data=data_read('data_files/GroceryList.xlsx - Daily meal plan.csv')
data2=data_read('data_files/GroceryList.xlsx - Grocery list.csv')
df=processing(data2)
pivot=processing1(data)
dt= processing2(data)
op=processing3(data)

st.markdown("<h1 style='text-align: center;'>📊 Most cooked Items</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label=str(op['dish'][0]),value=int(op['count'][0]))
with col2:
    st.metric(label=str(op['dish'][1]),value=int(op['count'][1]))
with col3:
    st.metric(label=str(op['dish'][2]),value=int(op['count'][2]))


st.markdown("<h1 style='text-align: center;'>list of finished items</h1>", unsafe_allow_html=True)
st.dataframe(df)


st.markdown("<h1 style='text-align: center;'>below is the cooking stats</h1>", unsafe_allow_html=True)
st.table(pivot)

st.markdown("<h1 style='text-align: center;'>Items cooked and there count</h1>", unsafe_allow_html=True)
st.dataframe(dt)