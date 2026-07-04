# 🐾 Pet Sales Dashboard

An interactive Sales Analytics Dashboard built with Python, Pandas, Matplotlib, and Streamlit** that allows users to upload a CSV file and explore customer and pet sales data through filters, KPIs, and visualizations.



Every business generates data, but raw spreadsheets rarely tell a meaningful story.

Imagine you're working as a Data Analyst for a pet retail company. Every day, thousands of customers purchase food, toys, accessories, and grooming products for their pets. The sales team wants quick insights without manually filtering Excel sheets.

Questions such as:

* Which pet category has the most customers?
* How many customers signed up on a specific date?
* Which customers purchased dog products?
* How can managers explore the data without writing Python code?

This project answers those questions by transforming raw CSV data into an interactive dashboard where users can upload their dataset and analyze it in seconds.

The goal isn't just visualization—it's about making data accessible for everyone.

---

# 🎯 Project Objectives

* Upload and analyze CSV files
* Perform basic data preprocessing
* Explore customer and pet sales information
* Filter records dynamically
* Display business KPIs
* Visualize insights using charts
* Build a beginner-friendly analytics dashboard

---

# 🛠 Tech Stack

* Python
* Streamlit
* Pandas
* Matplotlib

---

# 📂 Project Structure

```
Pet-Sales-Dashboard/
│
├── app.py
├── pet_sales_data.csv
├── requirements.txt
├── README.md
└── images/
```

---

# 📊 Dataset

The dataset contains sample customer and sales information.

| Column        | Description          |
| ------------- | -------------------- |
| customer_id   | Unique customer ID   |
| customer_name | Customer name        |
| pet_type      | Type of pet          |
| city          | Customer city        |
| category      | Product category     |
| signup_date   | Customer signup date |
| order_id      | Order number         |
| revenue       | Revenue generated    |

---

# 🧹 Data Preprocessing

Before building the dashboard, the dataset is prepared using Pandas.

### Steps performed

### 1. Import the dataset

```python
df = pd.read_csv(uploaded_file)
```

---

### 2. Preview the dataset

```python
df.head()
```

---

### 3. Explore the dataset

* Check columns
* Understand numerical statistics
* Verify available categories

```python
df.describe()
df.columns
```

---

### 4. Convert date column

```python
df["signup_date"] = pd.to_datetime(df["signup_date"]).dt.date
```

This enables filtering records using Streamlit's date slider.

---

### 5. Filter data

Filter by

* Pet Type
* Customer ID
* Signup Date

using Pandas.

Example

```python
filtered_df = df[df["pet_type"] == selected_pet]
```

---

# 🚀 Features

✅ CSV Upload

Users can upload any CSV dataset.

---

✅ Data Preview

Display uploaded records instantly.

---

✅ Dataset Statistics

Generate descriptive statistics using Pandas.

---

✅ Dynamic Filters

* Pet Type
* Customer
* Signup Date

---

✅ KPI Cards

Display important business metrics.

---

✅ Interactive Sidebar

Easy navigation and filtering.

---

✅ Matplotlib Visualization

Visualize customer distribution across pet types.

---

# 📈 Dashboard Workflow

```
Upload CSV

↓

Read Dataset

↓

Preprocess Data

↓

Preview Dataset

↓

Apply Filters

↓

Generate KPIs

↓

Create Visualizations

↓

Business Insights
```

---

# 💡 Business Questions Solved

* Which pet category has the highest number of customers?
* Which customers signed up on a particular date?
* How many customers belong to each pet category?
* How quickly can sales data be explored without Excel?

---

# 📦 Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd Pet-Sales-Dashboard
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📋 Requirements

Create a file named **requirements.txt**

```
streamlit
pandas
matplotlib
```

Install

```bash
pip install -r requirements.txt
```

---

# 🎓 Learning Outcomes

Through this project, you'll learn:

* Reading CSV files with Pandas
* Data preprocessing
* Filtering datasets
* Date handling
* Building interactive dashboards
* Creating KPI cards
* Using Streamlit widgets
* Data visualization with Matplotlib
* Structuring a Python analytics project

---

# 🔮 Future Improvements

* Interactive Plotly charts
* Revenue trend analysis
* Monthly sales dashboard
* Profit analysis
* Download filtered data
* Authentication
* SQL database integration
* Power BI integration
* Machine Learning predictions
* Deployment on Streamlit Community Cloud

---

# 🤝 Contributing

Contributions, ideas, and improvements are always welcome.

If you'd like to enhance this dashboard, feel free to fork the repository, create a new branch, and submit a pull request.

---

# 👨‍💻 Author

**Mohd Jeeshan**

Aspiring Data Analyst | Business Analyst | AI & Data Engineering Enthusiast

Currently learning Python, SQL, Streamlit, Machine Learning, and Generative AI by building real-world projects and sharing the journey publicly.

If you found this project useful, consider giving it a ⭐ on GitHub.

