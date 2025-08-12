import os
import pandas as pd
from datetime import datetime


base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "..", "..", "data", "campaign_data.csv")


df = pd.read_csv(data_path)


df["date"] = pd.to_datetime(df["date"])


if 'CTR' not in df.columns:
    df['CTR'] = df['clicks'] / df['impressions']
if 'CPI' not in df.columns:
    df['CPI'] = df['spend'] / df['installs']
if 'ROAS' not in df.columns:
    df['ROAS'] = df['revenue'] / df['spend']


kpi_list = ["ROAS", "CPI", "CTR"]


def detect_anomalies_pct_change(series, pct_threshold=0.1):
    pct_change = series.pct_change().abs()
    return pct_change > pct_threshold


def detect_anomalies_abs_change(series, abs_threshold):
    abs_change = series.diff().abs()
    return abs_change > abs_threshold


abs_thresholds_map = {
    "ROAS": 0.5,   # Örnek eşik, istersen ayarla
    "CPI": 0.5,
    "CTR": 0.05
}

anomaly_records = []



for (app, country, platform), group in df.groupby(["app_name", "country", "platform"]):
    group_sorted = group.sort_values("date")
    for kpi in kpi_list:
        if kpi in group.columns:
            pct_anomalies = detect_anomalies_pct_change(group_sorted[kpi], pct_threshold=0.1)
            abs_threshold = abs_thresholds_map.get(kpi, 0.5)
            abs_anomalies = detect_anomalies_abs_change(group_sorted[kpi], abs_threshold)
            combined_anomalies = pct_anomalies | abs_anomalies

            for date, value, is_anomaly in zip(group_sorted["date"], group_sorted[kpi], combined_anomalies):
                if is_anomaly:
                    anomaly_records.append({
                        "date": date.strftime("%Y-%m-%d"),
                        "app_name": app,
                        "country": country,
                        "platform": platform,
                        "metric": kpi,
                        "value": value
                    })

anomalies_df = pd.DataFrame(anomaly_records)

output_path = os.path.join(base_dir, "..", "..", "reports", "daily_anomaly_report.csv")
anomalies_df.to_csv(output_path, index=False)

print(f"Anomaly detection completed. {len(anomalies_df)} anomalies saved to {output_path}")

