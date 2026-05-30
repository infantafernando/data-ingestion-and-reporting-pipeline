-- Daily weather summary for reporting
-- Replace project_id if needed.

SELECT
  DATE(forecast_time) AS forecast_date,
  ROUND(AVG(temperature_2m), 2) AS avg_temperature_c,
  ROUND(AVG(relative_humidity_2m), 2) AS avg_humidity_pct,
  ROUND(AVG(precipitation_probability), 2) AS avg_rain_probability_pct,
  ROUND(AVG(wind_speed_10m), 2) AS avg_wind_speed,
  ROUND(AVG(comfort_score), 2) AS avg_comfort_score,
  COUNT(*) AS hourly_records
FROM `YOUR_GCP_PROJECT_ID.weather_pipeline.hourly_forecast`
GROUP BY forecast_date
ORDER BY forecast_date;
