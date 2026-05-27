-- ================================================
-- Sales & Revenue Analytics - SQL Queries
-- Dataset: Sample Superstore (9,994 orders)
-- ================================================

-- 1. Overall Business Performance
SELECT 
    COUNT(DISTINCT [Order ID]) as total_orders,
    COUNT(DISTINCT [Customer ID]) as total_customers,
    ROUND(SUM(Sales), 2) as total_sales,
    ROUND(SUM(Profit), 2) as total_profit,
    ROUND(AVG(Sales), 2) as avg_order_value,
    ROUND(SUM(Profit)/SUM(Sales)*100, 1) as profit_margin_pct
FROM superstore;

-- 2. Sales and Profit by Region
SELECT 
    Region,
    COUNT(DISTINCT [Order ID]) as orders,
    ROUND(SUM(Sales), 2) as total_sales,
    ROUND(SUM(Profit), 2) as total_profit,
    ROUND(SUM(Profit)/SUM(Sales)*100, 1) as profit_margin_pct
FROM superstore
GROUP BY Region
ORDER BY total_sales DESC;

-- 3. Sales and Profit by Category
SELECT 
    Category,
    ROUND(SUM(Sales), 2) as total_sales,
    ROUND(SUM(Profit), 2) as total_profit,
    ROUND(SUM(Profit)/SUM(Sales)*100, 1) as profit_margin_pct
FROM superstore
GROUP BY Category
ORDER BY total_sales DESC;

-- 4. Top 10 Sub-Categories by Sales
SELECT 
    [Sub-Category],
    ROUND(SUM(Sales), 2) as total_sales,
    ROUND(SUM(Profit), 2) as total_profit
FROM superstore
GROUP BY [Sub-Category]
ORDER BY total_sales DESC
LIMIT 10;

-- 5. Loss Making Sub-Categories
SELECT 
    [Sub-Category],
    ROUND(SUM(Sales), 2) as total_sales,
    ROUND(SUM(Profit), 2) as total_profit
FROM superstore
GROUP BY [Sub-Category]
HAVING total_profit < 0
ORDER BY total_profit ASC;

-- 6. Monthly Sales Trend
SELECT 
    strftime('%Y-%m', [O