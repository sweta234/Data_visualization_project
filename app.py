import streamlit as st
import pandas as pd
import help
import plotly.express as px
#import matplotlib.pyplot as plt
#import seaborn as sns
import plotly.figure_factory as ff

df = pd.read_csv('myntra.csv')
st.sidebar.title('MYNTRA DATA VIZ')
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Category', 'Individual_category','BrandName')
)
#df = pre.preprocess()
st.dataframe(df)

if user_menu == 'Category':
    st.header('indvidual_Category')
    Category_inv = help.Brand_category(df)
    selected_Category = st.sidebar.selectbox('select category',Category_inv  )
    Category = help.brand(selected_Category, df)
    st.dataframe(Category)

if user_menu == 'Individual_category':
    Individual_category = help.Individual_category(df)
    st.dataframe(Individual_category)
if user_menu == 'BrandName':
    BrandName = help.BrandName(df)
    st.dataframe(BrandName)