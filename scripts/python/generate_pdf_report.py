import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime

df = pd.read_csv("data/campaign_data.csv")

# KPI Control
if 'CTR' not in df.columns:
    df['CTR'] = df['clicks'] / df['impressions']
if 'CVR' not in df.columns:
    df['CVR'] = df['installs'] / df['clicks']
if 'CPI' not in df.columns:
    df['CPI'] = df['spend'] / df['installs']
if 'ROAS' not in df.columns:
    df['ROAS'] = df['revenue'] / df['spend']
if 'ARPU' not in df.columns:
    df['ARPU'] = df['revenue'] / df['installs']
if 'LTV' not in df.columns:
    df['LTV'] = df['ARPU'] * 90  # örnek LTV hesabı (90 gün)

# ROAS Graph
plt.figure(figsize=(8, 4))
df.groupby("country")["ROAS"].mean().sort_values().plot(kind='bar', color='skyblue')
plt.title("Average ROAS by Country")
plt.ylabel("ROAS")
plt.tight_layout()
plt.savefig("reports/roas_chart.png")
plt.close()

# PDF Class
class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 16)
        self.cell(0, 10, 'Daily Performance Marketing Report', ln=True, align='C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()} / {{nb}}', align='C')

# PDF
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()


pdf.set_font("Helvetica", size=12)
pdf.cell(0, 10, f"Date: {datetime.now().strftime('%Y-%m-%d')}", ln=True)
pdf.ln(5)


pdf.set_font("Helvetica", 'B', 10)
columns = ['country', 'platform', 'CTR', 'CVR', 'CPI', 'ROAS', 'ARPU', 'LTV']
col_widths = [25, 20, 20, 20, 20, 20, 20, 20]

for col, w in zip(columns, col_widths):
    pdf.cell(w, 8, col.upper(), border=1)
pdf.ln()

pdf.set_font("Helvetica", size=9)
for _, row in df[columns].head(20).iterrows():
    for col, w in zip(columns, col_widths):
        val = row[col]
        if isinstance(val, float):
            pdf.cell(w, 8, f"{val:.2f}", border=1)
        else:
            pdf.cell(w, 8, str(val), border=1)
    pdf.ln()

pdf.ln(10)


pdf.image("reports/roas_chart.png", w=170)

# save
pdf.output("reports/daily_anomaly_report.pdf")

