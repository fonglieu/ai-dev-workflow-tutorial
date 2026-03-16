import streamlit as st
import pandas as pd
import plotly.express as px

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

# T007: Aggregate sales by month
monthly_sales = (
    df.groupby(df["date"].dt.to_period("M"))["total_amount"]
    .sum()
    .reset_index()
)
monthly_sales["date"] = monthly_sales["date"].dt.to_timestamp()
monthly_sales = monthly_sales.sort_values("date")

# T008: Monthly sales trend line chart
fig = px.line(
    monthly_sales,
    x="date",
    y="total_amount",
    labels={"date": "Month", "total_amount": "Sales ($)"},
    title="Monthly Sales Trend",
    hover_data={"date": "|%B %Y", "total_amount": ":,.0f"},
)
fig.update_traces(mode="lines+markers")
st.plotly_chart(fig, use_container_width=True)
