import streamlit as st
import pandas as pd
import datetime
import plotly.express as px
st.header('Super Store DATA')
st.subheader('Top stats')
data=pd.read_csv('/workspaces/dashboard3/mentornow/superSales.csv')
st.write(data)
product_line=data['Product_line'].unique()
options=st.sidebar.selectbox('select product',(product_line))
df=data[data['Product_line']==options]

col1,col2=st.columns(2)
with col1:
 st.metric('Total Invoices',df['Invoice_ID'].size)
with col2:
 st.metric('Average rating',round(df['Rating'].mean(),2))

#st.markdown("""
    #<style>

col4,col5,col6=st.columns(3)
with col4:
    st.metric('Income',round(df['Total_price'].sum()))
with col5:
 st.metric('costs',round(df['costs'].sum()))
with col6:
 st.metric('Profit',round(df['Total_price'].sum())-round(df['costs'].sum()))

df['Order_date_new']=pd.to_datetime(df['Order_date'])


df1 = df[df['Order_date_new'].dt.month==3]


df1['date'] = df1['Order_date_new'].dt.day

# st.write(df1)


result = df1.groupby('date')['Quantity'].sum().reset_index()
st.write(result)
   

    
fig=px.line(data_frame=result,x='date',y='Quantity')
st.plotly_chart(fig)