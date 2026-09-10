import streamlit as st
import pandas as pd 
import time

st.set_page_config(page_title="Dashboard")

st.title("Dashboard")

st.write("Vložte export.")

uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

def missing_numbers(numbers, start, end):
    numbers = pd.Series(numbers).dropna().astype(int)
    numbers = numbers[(numbers >= start) & (numbers <= end)]
    numbers=numbers.sort_values().unique()
    expected = pd.RangeIndex(start, end + 1)
    # Find missing numbers
    missing = expected.difference(numbers)
    if len(missing) == 0:
        return pd.DataFrame(columns=["first_missing", "count"])
    # Convert to Series
    missing = pd.Series(missing.to_numpy())
    # Identify breaks between consecutive missing numbers
    groups = missing.diff().ne(1).cumsum()
    # Group consecutive missing numbers
    result = (
        missing.groupby(groups)
        .agg(first_missing="first", count="size")
        .reset_index(drop=True)
    )
    return result


if uploaded_file is not None:
    st.success("File uploaded successfully!")
    df = pd.read_csv(uploaded_file)
    if "Checked In" in df.columns:
        st.write(df["Checked In"].value_counts())
    if "Category" in df.columns:
        st.write(df["Category"].value_counts())

    number_range = st.slider("Vyber rozsah čísel", min_value=1, max_value=12000, value=(0,12000), step=100)
    st.write("Chybajúce čísla v rozsahu")
    st.write(missing_numbers(df["BIB"], number_range[0], number_range[1]))



    


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