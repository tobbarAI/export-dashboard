import streamlit as st
import pandas as pd 
import time

st.set_page_config(page_title="Dashboard")

st.title("Dmka Dashboard")

st.write("Vložte export.")

uploaded_file = st.file_uploader("Vyberte súbor", type=["csv", "xlsx"])

def missing_numbers(numbers, start, end):
    all_numbers = set(range(start, end + 1))
    present_numbers = set(int(x) for x in numbers if pd.notnull(x))
    missing = sorted(all_numbers - present_numbers)
    return pd.DataFrame({'Missing Numbers': missing})


if uploaded_file is not None:
    st.success("File uploaded successfully!")
    df = pd.read_csv(uploaded_file)
    if "Checked In" in df.columns:
        st.write(df["Checked In"].value_counts())
    if "Category" in df.columns:
        st.write(df["Category"].value_counts())
    if "Checked In" in df.columns and "Category" in df.columns:
        category_checkin = pd.crosstab(df["Category"],df["Checked In"])

    st.dataframe(category_checkin)

    number_range = st.slider("Vyber rozsah čísel:", min_value=1, max_value=12000, value=(1,12000), step=100)
    st.write("Chybajúce čísla v rozsahu")
    st.write(missing_numbers(df["Bib"], number_range[0], number_range[1]).head(10))



    


try:
    st. write("")
except Exception as e:
    st.error("❌ Repository import failed")
    st.exception(e)

st.divider()

st.write("If you can see this page, the Streamlit app itself is running correctly.")
