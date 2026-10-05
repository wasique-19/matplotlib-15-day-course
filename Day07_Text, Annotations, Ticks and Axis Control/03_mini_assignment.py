import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# -------------------------
# Build the expense data
# -------------------------
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Expenses": [1850, 2100, 1750, 2300, 1950, 2200],
})

# -------------------------
# Build the chart
# -------------------------
fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(df["Month"], df["Expenses"], marker="o", color="steelblue", linewidth=2)

ax.set_title("Monthly Expenses")
ax.set_xlabel("Month")
ax.set_ylabel("Expenses")

# Rotate month labels (not strictly needed for 6 short labels, but kept for consistency)
ax.set_xticklabels(df["Month"], rotation=45, ha="right")

# Currency-formatted y-axis
def currency_formatter(value, pos):
    return f"${value:,.0f}"

ax.yaxis.set_major_formatter(FuncFormatter(currency_formatter))

# Annotate the highest-expense month
max_idx = df["Expenses"].idxmax()
max_month = df.loc[max_idx, "Month"]
max_value = df.loc[max_idx, "Expenses"]

ax.annotate(
    f"Highest: ${max_value:,} ({max_month})",
    xy=(max_idx, max_value),
    xytext=(max_idx - 1.5, max_value + 150),
    arrowprops=dict(facecolor="darkred", arrowstyle="->"),
    fontsize=9,
)

ax.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()

# Save before showing
plt.savefig("annotated_expenses.png", dpi=150)
plt.show()