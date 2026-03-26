import streamlit as st
import pandas as pd

st.title("Sales Dashboard")
st.subheader("Filter sales by category")

import pandas as pd

data =  {
    'Product': ['Laptop', 'Smartphone', 'Desk Chair', 'Monitor', 'Keyboard'],
    'Category': ['Electronics', 'Electronics', 'Furniture', 'Electronics', 'Accessories'],
    'Sales': [1200, 800, 250, 400, 75]
}

df =  pd.DataFrame(data)


#Added a selectbox that lets the user filter the table by Category and added the filtered DataFrame using st.dataframe()
Category_table = st.sidebar.selectbox("Filter Category:", options=df['Category'].unique())

#Displayed the filtered DataFrame using st.dataframe()
filtered_df = df[df['Category'] == Category_table]
st.dataframe(filtered_df)

#line chart of Sales values for the selected category using st.line_chart()
st.write("Sales Trend")
st.line_chart(filtered_df['Sales'])