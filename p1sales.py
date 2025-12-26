import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------- LOAD CSV (LOCAL FILE PATH) ----------
df = pd.read_csv("C:/Fashion_Retail_Sales.csv", encoding="latin1")

print(df.head())
print(df.columns)

# --------- DATA CLEANING ----------
df.drop_duplicates(inplace=True)
df.ffill(inplace=True)

# --------- DATE COLUMN ----------
if 'Date Purchase' in df.columns:
    df['Date Purchase'] = pd.to_datetime(df['Date Purchase'])
else:
    print("Warning: 'Date Purchase' column not found. Date-based analysis might be affected.")

# --------- SALES COLUMN ----------
if 'Sales' not in df.columns and 'Purchase Amount (USD)' in df.columns:
    df['Sales'] = df['Purchase Amount (USD)']
elif 'Sales' in df.columns:
    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
    df.ffill(inplace=True)
else:
    print("Warning: 'Sales' or 'Purchase Amount (USD)' column not found for sales calculations.")

# --------- PRODUCT CATEGORY ----------
if 'Item Purchased' in df.columns:
    df['Product_Category'] = df['Item Purchased']
else:
    print("Warning: 'Item Purchased' column not found. Product category analysis might be affected.")

# --------- LINE PLOT ----------
if 'Date Purchase' in df.columns and 'Sales' in df.columns:
    sales_trend = df.groupby('Date Purchase')['Sales'].sum()

    plt.figure(figsize=(8,4))
    plt.plot(sales_trend.index, sales_trend.values, color='blue')
    plt.title("Sales Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("Cannot plot Sales Trend")

# --------- BAR CHART ----------
if 'Product_Category' in df.columns and 'Sales' in df.columns:
    product_sales = df.groupby('Product_Category')['Sales'].sum()

    plt.figure(figsize=(8,4))
    plt.bar(product_sales.index, product_sales.values, color='orange')
    plt.title("Sales by Product Category")
    plt.xlabel("Product Category")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("Cannot plot Sales by Product Category")

# --------- HEATMAP ----------
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
