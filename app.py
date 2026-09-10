import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard")

st.title("Dashboard")

st.write("Vložte export.")

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


df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4, 5],
    'Column 2': [6, 7, 8, 9, 10]
})

df