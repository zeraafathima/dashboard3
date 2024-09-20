import streamlit as st
import pandas as pd
st.header('Super Store DATA')
st.subheader('Top stats')
data=pd.read_csv('/workspaces/dashboard3/mentornow/superSales.csv')
st.write(data)
product_line=data['Product_line'].unique()
options=st.sidebar.selectbox('select product',(product_line))
df=data[data['Product_line']==options]

st.metric('Total Invoices',df['Invoice_ID'].size)

Average=st.metric('Average rating',round(df['Rating'].mean(),2))

    
