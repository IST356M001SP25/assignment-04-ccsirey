'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

# TODO Write code here to complete the unibrow.py

file  = st.file_uploader("Upload a file", type=['csv', 'json', 'xlsx'])

if file:
    file_ext = pl.get_file_extension(file.name)
    df = pl.load_file(file, file_ext)
    columns = pl.get_column_names(df)
    select_columns = st.multiselect("Select columns", options=columns)
    tog = st.toggle("Add filters", value=False)
    if tog:
        st.write("Filters")
        stcols = st.columns(3)
        text_cols = pl.get_columns_of_type(df, 'object')
        filter_col = stcols[0].selectbox("Select column to filter", text_cols)
        if filter_col:
            unique =pl.get_unique_values(df, filter_col)
            val = stcols[1].selectbox("Select value to filter On", unique)
            df_show = df[df[filter_col] == val][select_columns]
    else:
        df_show = df[select_columns]
        
    st.dataframe(df_show)
    st.dataframe(df_show.describe())