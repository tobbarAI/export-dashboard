import streamlit as st

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