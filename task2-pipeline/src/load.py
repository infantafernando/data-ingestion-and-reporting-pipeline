import logging

import pandas as pd
from google.cloud import bigquery

logger = logging.getLogger(__name__)


def load_to_bigquery(df: pd.DataFrame, bq_config: dict) -> None:
    project_id = bq_config["project_id"]
    dataset_id = bq_config["dataset_id"]
    table_id = bq_config["table_id"]
    full_table_id = f"{project_id}.{dataset_id}.{table_id}"

    client = bigquery.Client(project=project_id)

    job_config = bigquery.LoadJobConfig(
        write_disposition=bq_config.get("write_disposition", "WRITE_APPEND"),
        autodetect=True,
    )

    logger.info("Loading %s rows into %s", len(df), full_table_id)
    load_job = client.load_table_from_dataframe(df, full_table_id, job_config=job_config)
    load_job.result()
    logger.info("BigQuery load completed")
