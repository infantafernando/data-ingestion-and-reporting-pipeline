# Task 2: Open-Meteo to BigQuery Pipeline

## API Choice

I chose Open-Meteo because it provides structured weather forecast data through a simple JSON API and does not require an API key. This keeps the pipeline reproducible and easy to run during review.

## Pipeline Overview

```text
Open-Meteo API
    ↓
Python extraction script
    ↓
Transformation layer
    ↓
BigQuery table
    ↓
SQL summary query / dashboard layer
```

## What the Pipeline Does

1. Calls the Open-Meteo forecast API for Chennai coordinates.
2. Retrieves hourly weather forecast data.
3. Flattens the JSON response into a tabular format.
4. Cleans and converts data types.
5. Adds derived analytical fields:
   - `temperature_band`
   - `rain_risk_level`
   - `comfort_score`
6. Loads the transformed data into BigQuery.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Authenticate with GCP:

```bash
gcloud auth application-default login
```

Update `config/config.yaml` with your GCP project ID.

## Run Locally Without BigQuery

```bash
python src/main.py --dry-run
```

This writes a CSV to `output/weather_forecast.csv`.

## Run and Load to BigQuery

```bash
python src/main.py
```

## BigQuery Setup

Create a dataset called:

```text
weather_pipeline
```

The script writes to:

```text
YOUR_GCP_PROJECT_ID.weather_pipeline.hourly_forecast
```

## SQL Summary

A sample analytical query is available at:

```text
sql/weather_summary.sql
```

It calculates daily averages for temperature, humidity, rain probability, wind speed, and comfort score.

## Error Handling

The pipeline handles:

- API request failures
- Invalid JSON responses
- Missing expected fields
- Type conversion issues
- Null forecast timestamps

## Production Thinking

### Scheduling

In production, I would schedule this pipeline using Cloud Scheduler triggering a Cloud Function, or Cloud Composer if the pipeline becomes part of a larger workflow with dependencies.

### Failure Monitoring

I would add:

- Cloud Logging alerts for failed runs
- Email/Slack notifications
- Retry logic for temporary API failures
- Dead-letter storage for failed payloads
- Row-count and freshness checks after each load

### Scaling to 10x Data Volume

For higher data volume, I would:

- Partition the BigQuery table by `forecast_time`
- Cluster by location or source if multiple locations are added
- Avoid full refreshes and use incremental loads
- Add deduplication keys
- Separate raw and transformed tables
- Use Cloud Composer for orchestration
- Add data quality checks before publishing data to reporting tables

## What I Would Improve With More Time

- Add automated tests
- Add schema enforcement instead of autodetect
- Add retries with exponential backoff
- Add a raw landing table before transformation
- Add a Looker Studio dashboard on top of the BigQuery table
