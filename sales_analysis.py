import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

# STEP 1: LOAD DATA
print("Loading data...")
df = pd.read_csv('Sample - Superstore.csv', encoding='latin-1')
print(f"Shape: {df.shape}")
print(df.head())
print("\nColumns:", df.columns.tolist())
# STEP 2: DATA CLEANING & KEY METRICS
print("\nCleaning data...")
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
df['Ship Days'] = (df['Ship Date'] - df['Order Date']).dt.days

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
profit_margin = (total_profit / total_sales) * 100
total_orders = df['Order ID'].nunique()
total_customers = df['Customer ID'].nunique()

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Profit Margin: {profit_margin:.1f}%")
print(f"Total Orders: {total_orders}")
print(f"Total Customers: {total_customers}")

print("\nSales by Region:")
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print(region_sales)

print("\nSales by Category:")
category_sales = df.groupby('Category')[['Sales','Profit']].sum()
print(category_sales)

print("\nTop 5 Sub-Categories by Sales:")
subcategory_sales = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).head(5)
print(subcategory_sales)

print("\nBottom 5 Sub-Categories by Profit:")
subcategory_profit = df.groupby('Sub-Category')['Profit'].sum().sort_values().head(5)
print(subcategory_profit)
# STEP 3: SAVE CHARTS
# Chart 1: Sales by Region
fig, ax = plt.subplots(figsize=(8,5))
region_sales.plot(kind='bar', ax=ax, color=['#2196F3','#4CAF50','#FF9800','#F44336'])
ax.set_title('Sales by Region', fontsize=14, fontweight='bold')
ax.set_ylabel('Total Sales ($)')
plt.xticks(rotation=0)
for i, v in enumerate(region_sales):
    ax.text(i, v+5000, f'${v:,.0f}', ha='center', fontsize=9, fontweight='bold')
plt.tight_layout()
plt.savefig('sales_by_region.png', dpi=150)
print("Saved: sales_by_region.png")

# Chart 2: Profit by Category
fig, ax = plt.subplots(figsize=(8,5))
category_sales['Profit'].plot(kind='bar', ax=ax, color=['#FF9800','#4CAF50','#2196F3'])
ax.set_title('Profit by Category', fontsize=14, fontweight='bold')
ax.set_ylabel('Total Profit ($)')
plt.xticks(rotation=0)
for i, v in enumerate(category_sales['Profit']):
    ax.text(i, v+1000, f'${v:,.0f}', ha='center', fontsize=9, fontweight='bold')
plt.tight_layout()
plt.savefig('profit_by_category.png', dpi=150)
print("Saved: profit_by_category.png")

# Chart 3: Monthly Sales Trend
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()
fig, ax = plt.subplots(figsize=(12,5))
monthly_sales.plot(kind='line', ax=ax, color='#2196F3', linewidth=2, marker='o', markersize=4)
ax.set_title('Monthly Sales Trend', fontsize=14, fontweight='bold')
ax.set_ylabel('Total Sales ($)')
ax.set_xlabel('Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_sales_trend.png', dpi=150)
print("Saved: monthly_sales_trend.png")

# Export clean data
df.to_csv('superstore_clean.csv', index=False)
print("Saved: superstore_clean.csv")
print("\nProject Complete!")