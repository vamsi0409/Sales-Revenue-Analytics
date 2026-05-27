import pandas as pd
import sqlite3

# Load data
df = pd.read_csv('Sample - Superstore.csv', encoding='latin-1')
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
df['Ship Days'] = (df['Ship Date'] - df['Order Date']).dt.days

# Create SQLite database
conn = sqlite3.connect('superstore.db')
df.to_sql('superstore', conn, if_exists='replace', index=False)
print("Database created successfully!")

queries = {
    "1. Overall Business Performance": """
        SELECT COUNT(DISTINCT "Order ID") as total_orders,
               COUNT(DISTINCT "Customer ID") as total_customers,
               ROUND(SUM(Sales), 2) as total_sales,
               ROUND(SUM(Profit), 2) as total_profit,
               ROUND(AVG(Sales), 2) as avg_order_value,
               ROUND(SUM(Profit)/SUM(Sales)*100, 1) as profit_margin_pct
        FROM superstore
    """,
    "2. Sales and Profit by Region": """
        SELECT Region,
               COUNT(DISTINCT "Order ID") as orders,
               ROUND(SUM(Sales), 2) as total_sales,
               ROUND(SUM(Profit), 2) as total_profit,
               ROUND(SUM(Profit)/SUM(Sales)*100, 1) as profit_margin_pct
        FROM superstore
        GROUP BY Region
        ORDER BY total_sales DESC
    """,
    "3. Sales and Profit by Category": """
        SELECT Category,
               ROUND(SUM(Sales), 2) as total_sales,
               ROUND(SUM(Profit), 2) as total_profit,
               ROUND(SUM(Profit)/SUM(Sales)*100, 1) as profit_margin_pct
        FROM superstore
        GROUP BY Category
        ORDER BY total_sales DESC
    """,
    "4. Top 10 Sub-Categories by Sales": """
        SELECT "Sub-Category",
               ROUND(SUM(Sales), 2) as total_sales,
               ROUND(SUM(Profit), 2) as total_profit
        FROM superstore
        GROUP BY "Sub-Category"
        ORDER BY total_sales DESC
        LIMIT 10
    """,
    "5. Loss Making Sub-Categories": """
        SELECT "Sub-Category",
               ROUND(SUM(Sales), 2) as total_sales,
               ROUND(SUM(Profit), 2) as total_profit
        FROM superstore
        GROUP BY "Sub-Category"
        HAVING total_profit < 0
        ORDER BY total_profit ASC
    """,
    "6. Monthly Sales Trend": """
        SELECT strftime('%Y-%m', "Order Date") as month,
               ROUND(SUM(Sales), 2) as monthly_sales,
               ROUND(SUM(Profit), 2) as monthly_profit
        FROM superstore
        GROUP BY month
        ORDER BY month
        LIMIT 12
    """,
    "7. Top 10 Customers by Revenue": """
        SELECT "Customer Name",
               COUNT(DISTINCT "Order ID") as total_orders,
               ROUND(SUM(Sales), 2) as total_sales,
               ROUND(SUM(Profit), 2) as total_profit
        FROM superstore
        GROUP BY "Customer Name"
        ORDER BY total_sales DESC
        LIMIT 10
    """,
    "8. Sales by Ship Mode": """
        SELECT "Ship Mode",
               COUNT(*) as total_orders,
               ROUND(SUM(Sales), 2) as total_sales,
               ROUND(AVG("Ship Days"), 1) as avg_ship_days
        FROM superstore
        GROUP BY "Ship Mode"
        ORDER BY total_sales DESC
    """
}

for name, query in queries.items():
    print(f"\n{'='*50}")
    print(f"{name}")
    print('='*50)
    result = pd.read_sql_query(query, conn)
    print(result.to_string(index=False))

conn.close()
print("\n\nAll SQL queries executed successfully!")