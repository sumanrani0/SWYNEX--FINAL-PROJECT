import pandas as pd

df = pd.read_csv(r"pandas 2.py/DATA_ANALYSIS.PY/clean_data11.csv")

print("first 10 rows")
print(df.head(10))

print(df.info())

print(df.describe())

total_sales = df["Price"].sum()
print("total sales")
print(total_sales)


total_quantity = df["Quantity"].sum()
print("total_quantity")
print(total_quantity)


sales_location = df.groupby("Delivery_Location")["NET AMOUNT"].sum().sort_values(ascending=False)
print(sales_location)


best_items = df.groupby("Item_Name")["Quantity"].sum().sort_values(ascending=False)
print(best_items)


customer_analysis = df.groupby("Customer_Type")["Price"].sum()
print(customer_analysis)