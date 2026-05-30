import logging
from typing import Any, Dict

import requests

logger = logging.getLogger(__name__)




def fetch_weather_data(api_config: dict) -> Dict[str, Any]:
    params = {
        "latitude": api_config["latitude"],
        "longitude": api_config["longitude"],
        "timezone": api_config.get("timezone", "auto"),
        "forecast_days": api_config.get("forecast_days", 3),
        "hourly": ",".join(api_config["hourly"]),
    }
    logger.info(
    "Fetching forecast for latitude=%s longitude=%s for %s days",
    api_config["latitude"],
    api_config["longitude"],
    api_config.get("forecast_days", 3),
)

    try:
        logger.info("Calling Open-Meteo API")
        response = requests.get(api_config["base_url"], params=params, timeout=30)
        response.raise_for_status()
        payload = response.json()
    except requests.exceptions.RequestException as exc:
        logger.exception("API request failed")
        raise RuntimeError(f"Failed to fetch data from API: {exc}") from exc
    except ValueError as exc:
        logger.exception("API returned invalid JSON")
        raise RuntimeError("API returned invalid JSON") from exc

    if "hourly" not in payload or "time" not in payload["hourly"]:
        raise ValueError("Unexpected API response: missing hourly time series data")

    logger.info("Fetched %s hourly records", len(payload["hourly"]["time"]))
    return payload
