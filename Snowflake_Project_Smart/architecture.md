# SmartBuy Architecture

```text
Source Data
     │
     ▼
Snowflake RAW Layer
     │
     ▼
DBT Sources
     │
     ▼
DBT Staging Models
     │
     ├── stg_customers
     ├── stg_products
     ├── stg_orders
     ├── stg_order_items
     └── stg_reviews
     │
     ▼
DBT Mart Models
     │
     ├── dim_customer
     ├── dim_product
     └── fact_sales
     │
     ▼
Snowpark Python
     │
     ▼
TextBlob Sentiment Analysis
     │
     ▼
AI.REVIEW_SENTIMENT
     │
     ▼
Business Insights
```
