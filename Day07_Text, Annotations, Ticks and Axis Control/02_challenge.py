import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

np.random.seed(42)

# -------------------------
# Simulate 12 months of traffic
# -------------------------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visitors = np.random.normal(30000, 6000, 12).astype(int)
visitors = np.clip(visitors, 10000, None)   # keep values realistic (no negatives)

# -------------------------
# Build the chart
# -------------------------
fig, ax = plt.subplots(figsize=(11, 6))
ax.plot(months, visitors, marker="o", color="steelblue", linewidth=2)

ax.set_title("Website Traffic Over 12 Months")
ax.set_xlabel("Month")
ax.set_ylabel("Visitors")

# Rotate x-axis labels
ax.set_xticklabels(months, rotation=45, ha="right")

# Comma-separated y-axis formatting
def comma_formatter(value, pos):
    return f"{value:,.0f}"

ax.yaxis.set_major_formatter(FuncFormatter(comma_formatter))

# Annotate the highest-traffic month
max_idx = np.argmax(visitors)
ax.annotate(
    f"Highest: {visitors[max_idx]:,} visitors\n({months[max_idx]})",
    xy=(max_idx, visitors[max_idx]),
    xytext=(max_idx - 2, visitors[max_idx] + 6000),
    arrowprops=dict(facecolor="green", arrowstyle="->"),
    fontsize=9,
)

# Annotate the lowest-traffic month
min_idx = np.argmin(visitors)
ax.annotate(
    f"Lowest: {visitors[min_idx]:,} visitors\n({months[min_idx]})",
    xy=(min_idx, visitors[min_idx]),
    xytext=(min_idx - 2, visitors[min_idx] - 8000),
    arrowprops=dict(facecolor="red", arrowstyle="->"),
    fontsize=9,
)

ax.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()