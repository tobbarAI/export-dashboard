import streamlit as st
import pandas as pd 
import time

st.set_page_config(page_title="Dashboard")
st.markdown("""
<style>
    /* Main page */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    /* Title */
    h1 {
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    /* KPI cards */
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        text-align: center;
    }

    .metric-title {
        color: #6b7280;
        font-family: Arial, sans-serif;
        font-size: 25px;
        margin-bottom: 8px;
    }

    .metric-value {
        font-size: 50px;
        font-weight: 700;
        color: #111827;
    }

    /* Section headers */
    .section-title {
        font-size: 20px;
        font-weight: 600;
        margin-top: 25px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.title("Dmka Dashboard")

st.write("Vložte export.")

uploaded_file = st.file_uploader("Vyberte súbor", type=["csv", "xlsx"])

def missing_numbers(numbers, start, end):
    all_numbers = set(range(start, end + 1))
    present_numbers = set(int(x) for x in numbers if pd.notnull(x))
    missing = sorted(all_numbers - present_numbers)
    return pd.DataFrame({'Missing Numbers': missing})


if uploaded_file is not None:
    st.success("Súbor bol úspešne nahraný!")
    col1, col2 = st.columns(2)
    df = pd.read_csv(uploaded_file)
    #if "Checked In" in df.columns:
    #    col1.write(df["Checked In"].value_counts().reindex(["Yes", "No"], fill_value=0))
    #if "Category" in df.columns:
        #col2.write(df["Category"].value_counts())
    if "Checked In" in df.columns and "Category" in df.columns:
        category_checkin = pd.crosstab(df["Category"],df["Checked In"])
        category_checkin = pd.crosstab(df["Category"], df["Checked In"]).reindex(columns=["Yes", "No"],fill_value=0)
        category_checkin["Checked In %"] = (category_checkin["Yes"] /(category_checkin["Yes"] + category_checkin["No"]) * 100).round(1)

    total = len(df)
    checked_in = (df["Checked In"] == "Yes").sum()
    not_checked_in = (df["Checked In"] == "No").sum()
    checked_in_pct = checked_in / total * 100 if total > 0 else 0
    

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Počet bežcov</div>
            <div class="metric-value">{total:,}</div>
        </div>
        """, unsafe_allow_html=True)
    

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Odprezentovaní</div>
            <div class="metric-value" style="color: #10b981;">{checked_in:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Neodprezentovaní</div>
            <div class="metric-value" style="color: #ef4444;">{not_checked_in:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">V percentách</div>
            <div class="metric-value">{checked_in_pct:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.dataframe(category_checkin)

    number_range = st.slider("Vyber rozsah čísel:", min_value=1, max_value=12000, value=(1,12000), step=100)
    st.write("Chybajúce čísla v rozsahu")
    st.write(missing_numbers(df["Bib"], number_range[0], number_range[1]).head(10))
    st.divider()
    st.write(df[['First Name', 'Last Name','Email', 'Bib', 'Category', 'Checked In']].sort_values(by='Bib').set_index('Bib'))

    st.divider()

    st.markdown("""
    <style>
        [data-testid="stDataFrame"] {
            font-size:56px;
        }
    </style>
    """, unsafe_allow_html=True)

    
    

    table = (
    df[['First Name', 'Last Name', 'Email', 'Bib', 'Category', 'Checked In']]
    .sort_values(by='Bib')
    .set_index('Bib'))

    st.dataframe(
    table,
    use_container_width=True,
    row_height=45)



st.divider()



st.write("If you can see this page, the Streamlit app itself is running correctly.")
