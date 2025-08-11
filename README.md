# Mobile-Performance-Marketing-Insights-Simulation
A data analysis project that collects and analyzes data from advertising campaigns run by 20+ mobile applications in different countries and offers optimization suggestions.



Project Steps

1️⃣ Data Collection & Cleaning
Purpose: Combining campaign data from multiple sources into a single dataset.

Scope:

campaign_data.csv (KPIs: impressions, clicks, installs, spend, revenue, country, app_name, date)

Data extraction with SQL query (BigQuery/Snowflake scenario).

Purpose: Cleaning with Python pandas: missing data, outlier checking.

Qualification Requirement: SQL + Python + data preparation skills.

2️⃣ Performance Marketing KPI Calculations
Purpose: Measuring campaign health using the KPIs highlighted in the ad (CPI, CTR, ROAS, LTV).

Scope:

Calculating KPI formulas with Python.

Breakdown by country, platform (iOS/Android), and application.

Automatic export to Excel.

Qualification Requirement: Analytical skills, advanced level of Excel.

3️⃣ Dashboard & Automated Reporting
Purpose: Quickly deliver daily/weekly/monthly reports.

Scope:

Campaign Performance Dashboard with Power BI or Tableau (20 apps, 25 countries).

Automatic PDF report with Python (matplotlib + seaborn charts).

Quality: Dashboard creation, reporting, and visualization.

4️⃣ Detailed Campaign Monitoring & Anomaly Detection
Purpose: Continuously monitor active campaigns and detect abnormal fluctuations.

Scope:

Trend change detection with Python scipy or statsmodels.

Alert the marketing team with the "Daily Anomaly Report."

Quality: In-depth data analysis and detailed tracking.

5️⃣ Insights and Optimization Recommendations
Purpose: Generate actionable recommendations to guide the marketing and UA teams.

Scope:

KPI comparisons (e.g., countries with low Android CPI but high ROAS → budget increase recommendation).

Strategic recommendations via text file (insights.md).

Quality compensation: Data-driven decision support, campaign optimization.

## 🧩 Project Structure

```bash
mobile_perf_insights/
│
├── data/
│   ├── campaign_data.csv
│   ├── app_metadata.csv
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_kpi_analysis.ipynb
│   ├── 03_dashboard_export.ipynb
│
├── dashboards/
│   ├── performance_dashboard.pbix
│
├── reports/
│   ├── daily_anomaly_report.pdf
│   ├── insights.md
│
├── scripts/
│   ├── sql/
│   │   ├── fetch_campaign_data.sql
│   ├── python/
│   │   ├── generate_kpi_report.py
│   │   ├── anomaly_detection.py
│
└── README.md

```
