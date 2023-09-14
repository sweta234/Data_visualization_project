import streamlit as st

import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_excel('air.xlsx')

list_of_City = list(df['City'].unique())  
#list_of_City.insert(0,'Overall City')

#list_of_year = list(df['year'].unique())
#list_of_year.insert(0,'Overall India')

st.sidebar.title('India City Air polution visualization')

#selected_city = st.sidebar.selectbox('Select a state',list_of_City)
list_of_year = st.sidebar.selectbox('select year',list_of_City)



primary = st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[0:13]))
#secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')
#hover_data=['text']


if plot:

    #st.text('Size represent primary parameter')
    #st.text('Color represents secondary parameter')
    city_df = df[df['City'] == list_of_City]
        
    fig = px.scatter_mapbox(city_df, lat='Latitude', lon= 'Longitude',size=primary, zoom=4,size_max=35,
                                mapbox_style="carto-positron",width=1200,height=700,hover_name='City')

    st.plotly_chart(fig,use_container_width=True)

else:
    pass

