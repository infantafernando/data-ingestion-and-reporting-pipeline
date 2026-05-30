import logging
from datetime import datetime, timezone

import pandas as pd

logger = logging.getLogger(__name__)


def transform_weather_data(payload: dict) -> pd.DataFrame:
    hourly = payload["hourly"]
    df = pd.DataFrame(hourly)

    required_columns = [
        "time",
        "temperature_2m",
        "relative_humidity_2m",
        "precipitation_probability",
        "wind_speed_10m",
    ]

    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing expected columns: {missing}")

    df["forecast_time"] = pd.to_datetime(df["time"])
    df = df.drop(columns=["time"])

    numeric_cols = [
        "temperature_2m",
        "relative_humidity_2m",
        "precipitation_probability",
        "wind_speed_10m",
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["temperature_band"] = pd.cut(
        df["temperature_2m"],
        bins=[-100, 20, 30, 100],
        labels=["cool", "warm", "hot"],
    ).astype("string")

    df["rain_risk_level"] = pd.cut(
        df["precipitation_probability"],
        bins=[-1, 30, 70, 100],
        labels=["low", "medium", "high"],
    ).astype("string")

    df["comfort_score"] = (
        100
        - (df["temperature_2m"] - 24).abs() * 3
        - df["relative_humidity_2m"].fillna(0) * 0.2
        - df["wind_speed_10m"].fillna(0) * 0.5
    ).round(2)

    df["latitude"] = payload.get("latitude")
    df["longitude"] = payload.get("longitude")
    df["timezone"] = payload.get("timezone")
    df["ingested_at_utc"] = datetime.now(timezone.utc)

    df = df.dropna(subset=["forecast_time"])
    logger.info("Transformed data into %s rows and %s columns", df.shape[0], df.shape[1])
    return df
