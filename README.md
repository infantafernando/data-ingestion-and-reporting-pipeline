# Data & AI Product Engineer Assessment / NIVA Prep Project

This repository contains two compact, practical exercises:

1. **Product Scoping** — a v1 internal marketing performance tool.
2. **Pipeline Building** — a Python pipeline that extracts weather forecast data from Open-Meteo, transforms it, and loads it into BigQuery.

The goal is not to overbuild. The goal is to demonstrate clear data engineering thinking: source ingestion, transformation, warehouse loading, analytical SQL, and production-readiness.

## Repository Structure

```text
.
├── task1-product-scoping/
│   ├── product_brief.md
│   └── walkthrough.md
├── task2-pipeline/
│   ├── README.md
│   ├── config/config.yaml
│   ├── requirements.txt
│   ├── src/
│   │   ├── config.py
│   │   ├── extract.py
│   │   ├── transform.py
│   │   ├── load.py
│   │   └── main.py
│   └── sql/weather_summary.sql
└── README.md
```

## Why this project

This project is intentionally small enough to explain fully, but complete enough to discuss in a technical interview: API ingestion, error handling, data cleaning, schema design, BigQuery loading, SQL analysis, and production scaling.
