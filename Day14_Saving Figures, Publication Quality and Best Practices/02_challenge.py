import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image   # pip install pillow

# -------------------------
# 1. Helper functions
# -------------------------
def set_report_style():
    """Apply a clean, consistent look to every chart that follows."""
    plt.rcParams.update({
        "figure.figsize": (8, 5),
        "font.size": 12,
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.color": "#CCCCCC",
        "grid.alpha": 0.5,
        "grid.linestyle": "--",
        "axes.axisbelow": True,
    })

def save_fig(fig, name, folder="figures", dpi=300):
    """Save a figure as PNG (at `dpi`) and PDF, close it, return the PNG path."""
    os.makedirs(folder, exist_ok=True)   # idempotent: safe to run repeatedly
    png_path = os.path.join(folder, f"{name}.png")
    pdf_path = os.path.join(folder, f"{name}.pdf")
    fig.savefig(png_path, dpi=dpi, bbox_inches="tight")
    fig.savefig(pdf_path, bbox_inches="tight")
    plt.close(fig)
    return png_path

# -------------------------
# Simulate one DataFrame for all three charts
# -------------------------
np.random.seed(42)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

ad_spend = np.linspace(2000, 5000, 12) + np.random.normal(0, 250, 12)
sales = ad_spend * 0.05 + np.linspace(0, 60, 12) + np.random.normal(0, 12, 12)

df = pd.DataFrame({"Month": months, "Ad_Spend": ad_spend, "Sales": sales})
df["Quarter"] = ["Q" + str(i // 3 + 1) for i in range(12)]

# -------------------------
# 2. Build the three charts
# -------------------------
set_report_style()
saved_pngs = []

# --- Chart 1: line (finding computed from the data) ---
growth = (df["Sales"].iloc[-1] - df["Sales"].iloc[0]) / df["Sales"].iloc[0] * 100
verb = "grew" if growth > 0 else "fell"

fig, ax = plt.subplots()
ax.plot(df["Month"], df["Sales"], marker="o", color="#2E5984", linewidth=2.5)
ax.set_title(f"Sales {verb} {abs(growth):.0f}% from January to December")
ax.set_xlabel("Month")
ax.set_ylabel("Sales (units)")
saved_pngs.append(save_fig(fig, "01_sales_trend"))

# --- Chart 2: bar ---
quarterly = df.groupby("Quarter")["Sales"].sum()
best_q = quarterly.idxmax()

fig, ax = plt.subplots()
colors = ["#D98E04" if q == best_q else "#9DB4CC" for q in quarterly.index]
ax.bar(quarterly.index, quarterly.values, color=colors)
ax.set_title(f"{best_q} was the strongest quarter for sales")
ax.set_xlabel("Quarter")
ax.set_ylabel("Total sales (units)")
saved_pngs.append(save_fig(fig, "02_quarterly_sales"))

# --- Chart 3: scatter with trend line ---
r = df["Ad_Spend"].corr(df["Sales"])
slope, intercept = np.polyfit(df["Ad_Spend"], df["Sales"], 1)
line_x = np.linspace(df["Ad_Spend"].min(), df["Ad_Spend"].max(), 100)

fig, ax = plt.subplots()
ax.scatter(df["Ad_Spend"], df["Sales"], color="#5A8F5A", s=70, edgecolor="black")
ax.plot(line_x, slope * line_x + intercept, color="#D55E00", linewidth=2, linestyle="--")
ax.set_title(f"Ad spend and sales rise together (r = {r:.2f})")
ax.set_xlabel("Ad spend ($)")
ax.set_ylabel("Sales (units)")
saved_pngs.append(save_fig(fig, "03_ad_spend_vs_sales"))

# -------------------------
# 4. Print the pixel size of each PNG
# -------------------------
print("PNG sizes (width x height in pixels):")
for path in saved_pngs:
    with Image.open(path) as img:
        w, h = img.size
    print(f"  {path}: {w} x {h}")

# -------------------------
# 5. Reset the style
# -------------------------
plt.rcdefaults()
print("Style reset to matplotlib defaults.")