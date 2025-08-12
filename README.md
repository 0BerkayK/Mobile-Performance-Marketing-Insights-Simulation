# Mobile-Performance-Marketing-Insights-Simulation
A data analysis project that collects and analyzes data from advertising campaigns run by 20+ mobile applications in different countries and offers optimization suggestions.



## 🎯 Purpose
- Calculate performance marketing KPIs (CPI, CTR, ROAS, LTV)
- Report campaigns on a daily/weekly/monthly basis
- Identify optimization opportunities through anomaly detection
- Provide data-driven recommendations to marketing and UA teams

---

## 📌 Project Steps

### 1️⃣ Data Collection & Cleaning
- Combine campaign data from different sources
- Extract data with SQL (BigQuery/Snowflake scenario)
- Clean data with Python (`pandas`): missing value, outlier check
- **Output:** `data/campaign_data.csv`

### 2️⃣ Performance Marketing KPI Calculations
- Calculate metrics such as CPI, CTR, ROAS, LTV
- Breakdown by country, platform (iOS/Android), and application
- Automatic export to Excel report format
- **Technology:** Python (pandas, openpyxl)

### 3️⃣ Dashboard & Automatic Reporting
- Campaign Performance Dashboard with Power BI / Tableau**
- Automatic PDF report with Python (charts: matplotlib, seaborn)
- **Outputs:**
- `dashboards/performance_dashboard.pbix`
- `reports/daily_anomaly_report.pdf`

### 4️⃣ Detailed Campaign Monitoring & Anomaly Detection
- Daily trend tracking
- Detection of abnormal performance changes
- Trend analysis with Python (`scipy`, `statsmodels`)
- **Output:** `reports/daily_anomaly_report.pdf`

### 5️⃣ Insights and Optimization Recommendations
- Strategic recommendations with KPI comparisons
- Budget allocation and country/app-based optimization recommendations
- **Output:** `reports/insights.md`

## 🧩 Project Structure

```bash
mobile_perf_insights/
│
├── data/
│   ├── campaign_data.csv
│   
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_kpi_analysis.ipynb
│   ├── 03_dashboard_export.ipynb
│
├── dashboards/
│   ├── performance_dashboard.pbix
│   ├── performance_dashboard_data.csv
│
├── reports/
│   ├── daily_anomaly_report.pdf
│   ├── insights.md
│   ├── daily_anomaly_report.csv
│   ├── kpi_report.xlsx
│   ├── roas_chart.png
│
├── scripts/
│   ├── python/
│   │   ├── generate_kpi_report.py
│   │   ├── anomaly_detection.py
│
└── README.md

```
