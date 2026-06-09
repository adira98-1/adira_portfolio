# SmartBuy: End-to-End Snowflake + DBT + AI Retail Analytics Platform

## Project Overview

SmartBuy is an end-to-end modern data platform built using Snowflake, DBT, Snowpark, Python, and AI.

The project simulates a retail e-commerce analytics platform where customer, product, order, and review data are transformed into business-ready datasets and enriched with AI-powered sentiment analysis.

---

## Architecture

RAW DATA

↓

Snowflake RAW Layer

↓

DBT Staging Layer

↓

DBT Mart Layer

↓

Snowpark Python Processing

↓

AI Sentiment Analysis

↓

Snowflake AI Reporting Tables

---

## Technologies Used

* Snowflake
* DBT
* Snowpark
* Python
* SQL
* Git
* TextBlob NLP

---

## Data Model

### Staging Models

* stg_customers
* stg_products
* stg_orders
* stg_order_items
* stg_reviews

### Mart Models

* dim_customer
* dim_product
* fact_sales

### AI Models

* review_sentiment

---

## AI Use Case

Customer reviews are processed using Natural Language Processing (NLP) to classify sentiment:

* Positive
* Negative
* Neutral

The results are stored back into Snowflake for reporting and analytics.

---

## Key Features

* Snowflake Data Warehouse
* DBT Data Transformations
* Star Schema Design
* Data Quality Testing
* Snowpark Integration
* AI Sentiment Analysis
* End-to-End Data Pipeline

---

## Future Enhancements

* Incremental DBT Models
* Snowflake Cortex AI
* Power BI Dashboard
* CI/CD with GitHub Actions
* Airflow Orchestration

---

## Author

Adira Kumar
Data Engineer
