# Azure Data Factory (ADF) Project README Template

# Project Title

Incremental Employee ETL Pipeline using Azure Data Factory

---

# 1. Project Overview

This project demonstrates an enterprise ETL pipeline built using Azure Data Factory (ADF) for incremental data ingestion, transformation, and loading.

The pipeline reads employee data from Azure SQL Database, processes incremental records using watermark logic, performs transformations using Data Flow, and loads the data into the target system.

---

# 2. Business Problem

The business required an automated and scalable ETL solution to:

* Load employee data incrementally
* Avoid duplicate records
* Reduce manual intervention
* Maintain historical tracking
* Support near real-time reporting

The existing process was manual and caused delays in reporting and duplicate data issues.

---

# 3. Solution Architecture

```text
Azure SQL Database
        ↓
ADF Pipeline
        ↓
Lookup Activity (Watermark)
        ↓
Copy Activity
        ↓
ADLS Gen2 Raw Layer
        ↓
Data Flow Transformations
        ↓
Target SQL / Snowflake
        ↓
Power BI Reporting
```

---

# 4. Technologies Used

| Technology         | Purpose                               |
| ------------------ | ------------------------------------- |
| Azure Data Factory | ETL orchestration                     |
| Azure SQL Database | Source system                         |
| ADLS Gen2          | Data lake storage                     |
| Data Flow          | Transformations                       |
| SQL                | Watermark logic and stored procedures |

---

# 5. Key Features

## Incremental Loading

* Watermark-based ingestion
* Reads only new/updated records
* Prevents duplicate processing

## Dynamic Pipelines

* Parameterized datasets
* Dynamic table/file handling
* Metadata-driven framework

## Error Handling

* Retry policies
* Failure notifications

## Monitoring

* Pipeline monitoring
* Audit logging
* Execution tracking

## Transformations

* Lookup
* Conditional Split
* Derived Column
* SCD Type 2

---

# 6. Pipeline Workflow

## Step 1 — Trigger Pipeline

Pipeline starts using:

* Schedule Trigger
* Tumbling Window Trigger
* Event Trigger

---

## Step 2 — Fetch Watermark

Lookup Activity reads last processed watermark value.

Example:

```sql
SELECT LastWatermarkValue
FROM WatermarkTable
WHERE TableName = 'Employee';
```

---

## Step 3 — Read Incremental Data

Copy Activity/Data Flow reads only new records.

Example:

```sql
SELECT *
FROM Employee
WHERE LastModifiedDate > @WatermarkValue
```

---

## Step 4 — Load Raw Data

Incremental data is loaded into ADLS raw layer.

---

## Step 5 — Transform Data

Data Flow performs:

* Filtering
* Null handling
* Column derivation
* Joins
* Deduplication
* SCD Type 2 processing

---

## Step 6 — Load Target

Processed data is loaded into:

* Azure SQL
* Snowflake
* Synapse

---

## Step 7 — Update Watermark

Stored Procedure updates latest processed watermark.

Example:

```sql
UPDATE WatermarkTable
SET LastWatermarkValue = @NewWatermark
WHERE TableName = 'Employee';
```

---

# 7. Incremental Load Flow

```text
Source Table
      ↓
Lookup Watermark
      ↓
Read Incremental Records
      ↓
Copy Activity
      ↓
Transform Data
      ↓
Load Target
      ↓
Update Watermark
```

---

# 8. SCD Type 2 Flow

```text
Source
   ↓
Lookup Target
   ↓
Conditional Split
   ↓
Changed Rows
   ↓
Expire Old Record
   ↓
Insert New Active Record
```

---

# 9. Real-Time Scenarios Handled

| Scenario            | Solution                    |
| ------------------- | --------------------------- |
| Duplicate records   | Watermark logic             |
| Pipeline failure    | Retry + rerun               |
| Dynamic tables      | Parameterized datasets      |
| Empty file          | Get Metadata + If Condition |
| API polling         | Until Activity              |
| Slow copy           | Parallel copy optimization  |
| Historical tracking | SCD Type 2                  |

---

# 10. Important ADF Activities Used

| Activity         | Purpose                        |
| ---------------- | ------------------------------ |
| Copy Activity    | Data ingestion                 |
| Lookup Activity  | Watermark/config retrieval     |
| Get Metadata     | File validation                |
| If Condition     | Conditional execution          |
| ForEach          | Multiple file/table processing |
| Stored Procedure | Audit/watermark update         |
| Execute Pipeline | Modular framework              |
| Until Activity   | Polling/retry logic            |

---

# 11. Data Flow Transformations Used

| Transformation    | Purpose                     |
| ----------------- | --------------------------- |
| Source            | Read data                   |
| Sink              | Write data                  |
| Lookup            | Compare source vs target    |
| Derived Column    | Create/update columns       |
| Conditional Split | Route rows                  |
| Alter Row         | Insert/update/delete policy |
| Aggregate         | Summaries                   |
| Join              | Combine datasets            |
| Filter            | Remove invalid rows         |

---

# 12. Error Handling Strategy

Implemented:

* Retry policy
* Logging table
* Failure notifications
* Watermark rollback
* Validation checks

---

# 13. Performance Optimization

Techniques used:

* Parallel copy
* Partitioning
* Filter pushdown
* Incremental ingestion
* Optimized Data Flow transformations
* Reusable datasets

---

# 14. Project Folder Structure

```text
ADF-Employee-ETL/
│
├── README.md
├── architecture/
├── pipelines/
├── datasets/
├── dataflows/
├── linked-services/
├── sql-scripts/
├── screenshots/
└── sample-data/
```

---

# 15. Sample Interview Explanation

"Designed and developed enterprise-scale Azure Data Factory pipelines for incremental ingestion from Azure SQL into ADLS and Snowflake using watermark logic, parameterized datasets, Data Flow transformations, stored procedures, and SCD Type 2 implementation."


Technologies: Azure Data Factory, Azure SQL, Databricks, Snowflake, SQL, Python
