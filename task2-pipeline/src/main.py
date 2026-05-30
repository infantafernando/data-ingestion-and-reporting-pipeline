import argparse
import logging
from pathlib import Path

from config import load_config
from extract import fetch_weather_data
from transform import transform_weather_data
from load import load_to_bigquery


def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Open-Meteo to BigQuery pipeline")
    parser.add_argument("--config", default="config/config.yaml", help="Path to config file")
    parser.add_argument("--dry-run", action="store_true", help="Run extract/transform without BigQuery load")
    parser.add_argument("--output", default="output/weather_forecast.csv", help="CSV output path for dry run")
    args = parser.parse_args()

    setup_logging()
    logger = logging.getLogger(__name__)

    cfg = load_config(args.config)
    payload = fetch_weather_data(cfg["api"])
    df = transform_weather_data(payload)

    if args.dry_run:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False)
        logger.info("Dry run complete. Wrote CSV to %s", output_path)
        return

    load_to_bigquery(df, cfg["bigquery"])


if __name__ == "__main__":
    main()
