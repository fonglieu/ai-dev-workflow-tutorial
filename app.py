import streamlit as st
import pandas as pd

# T003: Page configuration — must be first Streamlit call
st.set_page_config(
    page_title="ShopSmart Sales Dashboard",
    layout="wide"
)

# T003: Branded page header
st.title("ShopSmart Sales Dashboard")

# T004: Load sales data
df = pd.read_csv("data/sales-data.csv", parse_dates=["date"])

# T005: Compute KPIs
total_sales = df["total_amount"].sum()
total_orders = len(df)

# T006: KPI cards
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Sales", f"${total_sales:,.0f}")
with col2:
    st.metric("Total Orders", f"{total_orders:,}")
