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

# T013: Missing-file guard
DATA_PATH = "data/sales-data.csv"
if not __import__("os").path.exists(DATA_PATH):
    st.error(
        "Data file not found: `data/sales-data.csv`. "
        "Please ensure the file exists in the repository root before running the dashboard."
    )
    st.stop()

# T004: Load sales data
df = pd.read_csv(DATA_PATH, parse_dates=["date"])

# T012: CSV validation
REQUIRED_COLUMNS = {"date", "order_id", "product", "category", "region", "quantity", "unit_price", "total_amount"}
warnings = []
missing_cols = REQUIRED_COLUMNS - set(df.columns)
for col in sorted(missing_cols):
    warnings.append(f"Missing required column: `{col}`")

# T014: Sidebar warnings expander
if warnings:
    with st.sidebar.expander("⚠️ Data Warnings"):
        for w in warnings:
            st.write(w)

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

# T009 + T010: Aggregate sales by category and region
category_sales = (
    df.groupby("category")["total_amount"]
    .sum()
    .reset_index()
    .sort_values("total_amount", ascending=False)
)
region_sales = (
    df.groupby("region")["total_amount"]
    .sum()
    .reset_index()
    .sort_values("total_amount", ascending=False)
)

# T011: Side-by-side bar charts in two columns
col_cat, col_reg = st.columns(2)
with col_cat:
    fig_cat = px.bar(
        category_sales,
        x="category",
        y="total_amount",
        labels={"category": "Category", "total_amount": "Sales ($)"},
        title="Sales by Category",
    )
    st.plotly_chart(fig_cat, use_container_width=True)
with col_reg:
    fig_reg = px.bar(
        region_sales,
        x="region",
        y="total_amount",
        labels={"region": "Region", "total_amount": "Sales ($)"},
        title="Sales by Region",
    )
    st.plotly_chart(fig_reg, use_container_width=True)
