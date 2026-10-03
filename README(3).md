# 🍽️ Restaurant Sales & Customer Analysis

## 📌 Project Overview

This project is a complete data analytics case study based on restaurant sales and customer order data.

The objective of this project is to analyze restaurant orders and understand:

- Sales and revenue performance
- Popular food items
- Quantity sold by item
- Customer types
- Customer feedback
- Delivery-location performance
- Discounts
- Average order value
- Key business insights

The project follows a complete data analytics workflow:

**Raw Data → Data Cleaning → Data Analysis → Data Visualization → Dashboard → Business Insights**

---

## 🎯 Problem Statement

Restaurants generate large amounts of sales and customer data through their daily orders. Analyzing this data can help businesses understand which products are performing well, where orders are coming from, what customers think about their service, and how revenue is distributed.

The objective of this project is to analyze restaurant order data and identify meaningful patterns in sales, customer behavior, popular food items, feedback, delivery locations, and discounts.

The analysis is designed to provide business insights that can support data-driven decision-making.

---

# 📂 Dataset Information

The project dataset contains restaurant order information.

### Dataset Period

**1 April 2025 – 18 June 2025**

### Dataset Size

- **223 orders**
- **398 total quantity**
- **36 unique food items**
- **15 delivery locations**

### Dataset Columns

| Column | Description |
|---|---|
| `Order_ID` | Unique identifier for each order |
| `Date` | Date on which the order was placed |
| `Item_Name` | Name of the food item |
| `Quantity` | Quantity of the item ordered |
| `Price` | Price associated with the order/item |
| `DISCOUNT` | Discount applied to the order |
| `SUB TOTAL` | Amount before discount |
| `NET AMOUNT` | Final amount after discount |
| `Customer_Type` | New or Returning customer |
| `Feedback` | Customer feedback category |
| `Delivery_Location` | Location where the order was delivered |

---

# 🧹 Data Cleaning

The original dataset was not immediately ready for analysis, so a data-cleaning process was performed before visualization and analysis.

### Cleaning steps included:

1. Reviewed the raw dataset.
2. Corrected the dataset structure.
3. Separated improperly formatted data.
4. Standardized column names.
5. Checked for duplicate records.
6. Checked for missing values.
7. Corrected data types.
8. Standardized categorical values.
9. Prepared numerical columns for analysis.
10. Created calculated values such as subtotal and net amount.
11. Prepared the cleaned dataset for visualization and dashboard creation.

### Data Quality Check

The cleaned dataset contains:

- **223 records**
- **11 columns**

The workbook contains separate **UNCLEAN DATA** and **CLEAN DATA** sheets to show the transformation from the original data to the cleaned dataset.

---

# 🛠️ Tools & Technologies

The following tools were used in this project:

- **Microsoft Excel** – Data cleaning and initial data preparation
- **Python** – Data analysis
- **Pandas** – Data manipulation and aggregation
- **Power BI** – Interactive dashboard and visualization
- **GitHub** – Project documentation and version sharing

---

# 🐍 Python Data Analysis

Python and Pandas were used to perform basic exploratory analysis and calculate important metrics.

The analysis included:

- Inspecting the first rows of the dataset
- Checking dataset information
- Generating descriptive statistics
- Calculating total sales
- Calculating total quantity
- Analyzing sales by delivery location
- Identifying best-selling items
- Analyzing sales by customer type

### Example analysis

```python
import pandas as pd

df = pd.read_excel("CLEAN_DATASET.xlsx")

print(df.head(10))
print(df.info())
print(df.describe())

total_quantity = df["Quantity"].sum()
print(total_quantity)

sales_location = df.groupby("Delivery_Location")["NET AMOUNT"].sum().sort_values(ascending=False)
print(sales_location)

best_items = df.groupby("Item_Name")["Quantity"].sum().sort_values(ascending=False)
print(best_items)

customer_analysis = df.groupby("Customer_Type")["Price"].sum()
print(customer_analysis)
```

---

# 📊 Key Performance Indicators

| KPI | Result |
|---|---:|
| Total Orders | **223** |
| Total Quantity | **398** |
| Gross Subtotal | **₹107,960** |
| Total Discount | **₹1,555** |
| Net Revenue | **₹106,405** |
| Average Order Value | **₹477.15** |

### Average Order Value

**Net Revenue ÷ Total Orders**

**₹106,405 ÷ 223 = ₹477.15**

---

# 📈 Dashboard

An interactive **Restaurant Sales Dashboard** was created using Power BI.

The dashboard contains:

### KPI Cards

- Total Orders
- Total Quantity
- Total Revenue
- Average Order Value

### Visualizations

- Quantity by Item
- Orders by Feedback
- Orders by Delivery Location
- Discount by Item
- Revenue by Item

### Filters

- Delivery Location
- Customer Type

The dashboard allows users to interactively explore restaurant performance and identify patterns in sales, products, customers, feedback, locations, and discounts.

---

# 🍗 Top-Selling Items by Quantity

| Rank | Item | Quantity |
|---:|---|---:|
| 1 | Butter Naan | **32** |
| 2 | Chicken Biryani | **26** |
| 3 | Veg Pulao | **26** |
| 4 | Tandoori Roti | **24** |
| 5 | Garlic Naan | **24** |
| 6 | Dal Makhani | **21** |
| 7 | Mixed Veg Curry | **20** |
| 8 | Veg Biryani | **15** |
| 9 | Gulab Jamun | **15** |
| 10 | Butter Chicken | **14** |

---

# 💰 Top Items by Net Revenue

| Rank | Item | Net Revenue |
|---:|---|---:|
| 1 | Chicken Biryani | **₹12,860** |
| 2 | Veg Pulao | **₹8,690** |
| 3 | Mixed Veg Curry | **₹7,760** |
| 4 | Butter Chicken | **₹7,000** |
| 5 | Butter Naan | **₹5,780** |
| 6 | Veg Biryani | **₹4,990** |
| 7 | Garlic Naan | **₹4,290** |
| 8 | Dal Makhani | **₹4,050** |
| 9 | Veg Spring Rolls | **₹3,560** |
| 10 | Cheese Garlic Bread | **₹3,120** |

---

# 😊 Customer Feedback Analysis

| Feedback | Orders | Net Revenue |
|---|---:|---:|
| Good | **99** | **₹40,615** |
| Excellent | **73** | **₹35,320** |
| Average | **51** | **₹30,470** |
| **Total** | **223** | **₹106,405** |

**Good** was the most frequent feedback category, with 99 orders.

---

# 👥 Customer Type Analysis

| Customer Type | Orders | Net Revenue |
|---|---:|---:|
| New | **114** | **₹57,305** |
| Returning | **109** | **₹49,100** |
| **Total** | **223** | **₹106,405** |

There were **114 new-customer orders** and **109 returning-customer orders**.

---

# 📍 Delivery Location Analysis

| Delivery Location | Orders | Net Revenue |
|---|---:|---:|
| Greater Noida | 36 | ₹16,040 |
| Noida Sector 18 | 36 | ₹16,495 |
| Indirapuram | 32 | ₹15,260 |
| Vaishali | 32 | ₹17,460 |
| Noida Sector 62 | 32 | ₹13,080 |
| Noida Sector 15 | 32 | ₹15,260 |
| Connaught Place | 4 | ₹3,430 |
| Rajouri Garden | 3 | ₹1,700 |
| Hauz Khas | 3 | ₹1,270 |
| Na | 3 | ₹1,400 |
| Karol Bagh | 2 | ₹2,150 |
| Lajpat Nagar | 2 | ₹610 |
| Punjabi Bagh | 2 | ₹960 |
| Saket | 2 | ₹450 |
| Vasant Kunj | 2 | ₹840 |

**Greater Noida and Noida Sector 18 recorded the highest number of orders, with 36 orders each.**

> Note: The dataset contains `Na` as a delivery-location value for 3 orders. If this represents an unknown/missing location rather than an intentional category, it should be reviewed in a future data-quality update.

---

# 💡 Key Business Insights

### 1. Popular Product
**Butter Naan recorded the highest quantity sold, with 32 units.**

### 2. Highest Revenue Item
**Chicken Biryani generated the highest net revenue among the food items, at ₹12,860.**

### 3. Customer Feedback
**Good feedback was the most common feedback category, with 99 orders.**

### 4. New vs Returning Customers
The dataset contains **114 new-customer orders** and **109 returning-customer orders**.

### 5. Delivery Locations
**Greater Noida and Noida Sector 18 recorded the highest order count, with 36 orders each.**

### 6. Revenue by Location
Among the listed locations, **Vaishali generated the highest net revenue at ₹17,460**, with 32 orders.

### 7. Overall Revenue
The restaurant generated **₹106,405 in net revenue from 223 orders**, with an average order value of approximately **₹477.15**.

### 8. Discounts
A total discount amount of **₹1,555** was recorded across the dataset.

---

# 🔄 Project Workflow

```text
Raw Restaurant Data
        ↓
Data Cleaning
        ↓
Clean Dataset
        ↓
Exploratory Data Analysis
        ↓
Python / Pandas Analysis
        ↓
Power BI Visualization
        ↓
Interactive Dashboard
        ↓
Business Insights
        ↓
Final Case Study
```

---

# 📁 Project Structure

```text
Restaurant-Sales-Customer-Analysis/
│
├── README.md
│
├── Dataset/
│   └── CLEAN_DATASET.xlsx
│
├── Python/
│   └── data_analysis.py
│
├── Dashboard/
│   └── restaurant_dashboard.pbix
│
└── Images/
    └── restaurant_dashboard.png
```

---

# 📊 Project Deliverables

- ✅ Raw dataset
- ✅ Cleaned dataset
- ✅ Data-cleaning process
- ✅ Python analysis
- ✅ Exploratory analysis
- ✅ Power BI dashboard
- ✅ KPI calculations
- ✅ Business insights
- ✅ Project conclusion
- ✅ GitHub documentation

---

# 🏁 Conclusion

This project demonstrates the complete data analytics workflow using restaurant sales data.

The analysis covered sales performance, order quantity, customer types, customer feedback, delivery locations, discounts, and food-item performance.

The Power BI dashboard provides an interactive way to explore the data and monitor important business metrics.

The project demonstrates practical skills in:

**Data Cleaning → Data Analysis → Data Visualization → Dashboard Development → Business Insights**

---

# 👩‍💻 Author

**Suman**

### Skills Demonstrated

- Microsoft Excel
- Data Cleaning
- Python
- Pandas
- Power BI
- Data Visualization
- Exploratory Data Analysis
- Business Insights
- GitHub
