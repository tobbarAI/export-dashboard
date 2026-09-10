import streamlit as st
import pandas as pd 
import time

st.set_page_config(page_title="Dashboard")

st.title("Dashboard")

st.write("Vložte export.")

uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    df = pd.read_csv(uploaded_file)
    st.write(df["Checked In"].value_counts())



# Test your repository imports here
try:
    # Example:
    # from src.my_module import my_function

    st.success("✅ Repository imports work!")

except Exception as e:
    st.error("❌ Repository import failed")
    st.exception(e)

st.divider()

st.write("If you can see this page, the Streamlit app itself is running correctly.")

'''
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.DataFrame({
        'Column 1': [1, 2, 3, 4, 5],
        'Column 2': [6, 7, 8, 9, 12]
    })

st.dataframe(df.style.highlight_max(axis=0))'''