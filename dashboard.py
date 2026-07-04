import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configure the page
st.set_page_config(
    page_title="Sales Dashboard - Mohd Jeeshan",
    page_icon="😍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title(" Sales Dashboard - By Mohd Jeeshan")
st.write("Upload a CSV file and explore your data.")

# Upload CSV
uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

if uploaded_file:

    st.success("File uploaded successfully! 🎉")

    # Read the data
    df = pd.read_csv(uploaded_file)

    # Basic file details
    st.write(f"**File Name:** {uploaded_file.name}")
    st.write(f"**File Size:** {uploaded_file.size:,} bytes")

    # Preview dataset
    st.subheader("Data Preview")
    st.dataframe(df)

    # Dataset summary
    st.subheader("Quick Summary")
    st.write(df.describe())

    # Filter by pet type
    st.subheader("Filter by Pet Type")

    selected_pet = st.selectbox(
        "Choose a pet type",
        df["pet_type"].unique()
    )

    pet_data = df[df["pet_type"] == selected_pet]
    st.dataframe(pet_data)

    # Filter by customer
    st.subheader("Find Customer Records")

    selected_customers = st.multiselect(
        "Select Customer ID(s)",
        df["customer_id"].unique()
    )

    customer_data = df[
        df["customer_id"].isin(selected_customers)
    ]

    st.dataframe(customer_data)

    # Date filter
    st.subheader("Signup Date Filter")

    df["signup_date"] = pd.to_datetime(df["signup_date"]).dt.date

    selected_date = st.slider(
        "Select a signup date",
        min_value=df["signup_date"].min(),
        max_value=df["signup_date"].max(),
        value=df["signup_date"].min()
    )

    date_data = df[df["signup_date"] == selected_date]

    st.dataframe(date_data)

    # Dashboard KPIs
    st.subheader("Key Metrics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Revenue", "₹4,50,000", "+12%")
    col2.metric("Customers", "875", "+8%")
    col3.metric("Orders", "1,250", "+5%")

    # Sidebar filters
    st.sidebar.header("Filters")

    sidebar_pet = st.sidebar.selectbox(
        "Pet Type",
        df["pet_type"].unique()
    )

    # Optional filter form
    st.subheader("Additional Filters")

    with st.form("filter_form"):

        category = st.selectbox(
            "Category",
            ["All", "Electronics", "Fashion"]
        )

        city = st.multiselect(
            "City",
            ["Mumbai", "Delhi", "Chennai"]
        )

        apply = st.form_submit_button("Apply Filters")

    if apply:
        st.success("Filters applied successfully!")

    # Simple chart
    st.subheader("Pet Type Distribution")

    pet_count = df["pet_type"].value_counts()

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(pet_count.index, pet_count.values)

    ax.set_xlabel("Pet Type")
    ax.set_ylabel("Count")
    ax.set_title("Number of Customers by Pet Type")

    st.pyplot(fig)

else:
    st.info("Upload a CSV file to start exploring your data.")
