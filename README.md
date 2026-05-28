# Sales & Revenue Analytics

I built this project because I wanted to practice business intelligence 
analytics with real sales data. Every company has sales data, and being 
able to analyze it, find patterns, and make recommendations is one of 
the most valuable skills a data analyst can have.

## What I Did
I started with the Sample Superstore dataset — 9,994 orders across 4 
regions, 3 product categories, and 17 sub-categories. My goal was to 
answer a simple question: where is this business making money, and 
where is it losing it?

The most interesting finding was the Tables sub-category. It had $206,966 
in sales — looks impressive on the surface — but it was actually losing 
$17,725 in profit. That's the kind of insight that gets attention in a 
business meeting. High revenue doesn't always mean high profit.

I was also surprised by the regional gap. The West region had a 14.9% 
profit margin while Central was only 7.9%. Same company, same products, 
very different profitability. That's worth investigating further.

## Dashboard
[View Interactive Dashboard on Tableau Public](https://public.tableau.com/app/profile/vamsi.batchu8113/viz/SalesRevenueAnalyticsDashboard/SalesRevenueAnalyticsDashboard)

## Key Business Metrics
- **Total Sales: $2,297,200.86**
- **Total Profit: $286,397.02**
- **Profit Margin: 12.5%**
- **Total Orders: 5,009**
- **Total Customers: 793**

## Key Findings
- West region leads with $725,457 in sales — 31.6% of total revenue
- Technology is highest revenue category at $836,154
- **Tables sub-category losing $17,725** — biggest profit drain
- Phones and Chairs are top revenue drivers at $330K and $328K
- South region underperforming at $391,721 — 41% below West

## Sales by Region
| Region | Sales |
|--------|-------|
| West | $725,457 |
| East | $678,781 |
| Central | $501,239 |
| South | $391,721 |

## Sales by Category
| Category | Sales | Profit |
|----------|-------|--------|
| Technology | $836,154 | $145,454 |
| Furniture | $741,999 | $18,451 |
| Office Supplies | $719,047 | $122,490 |

## SQL Analysis
I wrote 8 SQL queries to extract business insights:
- Overall business performance metrics
- Sales and profit breakdown by region
- Category-level profitability analysis
- Top 10 sub-categories by sales
- Loss-making sub-categories identification
- Monthly sales trend analysis
- Top 10 customers by revenue
- Sales breakdown by shipping mode

The SQL analysis revealed that Sean Miller is the top customer at 
$25,043 in sales but actually losing the company $1,980 in profit — 
another counterintuitive finding worth flagging to a sales team.

## Tools Used
- Python (Pandas, NumPy, Matplotlib)
- SQL
- Tableau

## Files
- `sales_analysis.py` — Complete Python analysis
- `sales_queries.sql` — 8 SQL business queries
- `run_sales_sql.py` — SQL execution script
- `sales_by_region.png` — Regional sales chart
- `profit_by_category.png` — Category profit chart
- `monthly_sales_trend.png` — Monthly trend chart
- `superstore_clean.csv` — Cleaned dataset for dashboard

## What I Learned
This project reinforced something important — revenue and profit are 
very different things. The Tables sub-category looked like a strong 
performer based on sales alone, but the SQL analysis revealed it was 
the biggest profit drain in the entire dataset. That's exactly the 
kind of analysis that helps businesses make better decisions.
