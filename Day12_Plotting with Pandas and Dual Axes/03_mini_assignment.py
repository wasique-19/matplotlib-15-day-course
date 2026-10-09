"""Day 12 - Mini Assignment: Store Performance Dashboard (Mini)"""

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# Data
# -------------------------
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Revenue": [200, 220, 260, 240, 300, 340],
    "Orders": [80, 90, 105, 100, 120, 135],
    "Returns %": [4.5, 4.1, 3.8, 4.0, 3.5, 3.2],
})

BAR_COLOR = "#2E5984"    # Revenue (left axis)
LINE_COLOR = "#D9534F"   # Returns % (right axis)

# -------------------------
# Task 1: Revenue and Orders as a two-panel subplots=True chart
# -------------------------
axes = df.set_index("Month")[["Revenue", "Orders"]].plot(
    subplots=True, marker="o", figsize=(8, 6), legend=False,
    color=[BAR_COLOR, "#5A8F5A"],
)
axes[0].set_title("Monthly Revenue")
axes[0].set_ylabel("Revenue")
axes[1].set_title("Monthly Orders")
axes[1].set_ylabel("Orders (count)")
axes[1].set_xlabel("Month")
for ax in axes:
    ax.grid(True, linestyle="--", alpha=0.5)

plt.suptitle("Revenue and Orders, Jan to Jun", fontsize=14, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("two_panel_revenue_orders.png", dpi=150)
plt.show()

# -------------------------
# Task 2 and 3: Dual-axis chart (Revenue bars + Returns % line)
# -------------------------
fig, ax1 = plt.subplots(figsize=(9, 5))

ax1.bar(df["Month"], df["Revenue"], color=BAR_COLOR, alpha=0.85, label="Revenue")
ax1.set_xlabel("Month")
ax1.set_ylabel("Revenue", color=BAR_COLOR)
ax1.tick_params(axis="y", labelcolor=BAR_COLOR)
ax1.grid(True, axis="y", linestyle="--", alpha=0.4)

ax2 = ax1.twinx()
ax2.plot(df["Month"], df["Returns %"], color=LINE_COLOR, marker="o",
         linewidth=2.5, label="Returns %")
ax2.set_ylabel("Returns (%)", color=LINE_COLOR)
ax2.tick_params(axis="y", labelcolor=LINE_COLOR)
ax2.set_ylim(0, 6)

# Merged legend
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left")

ax1.set_title("Revenue vs Returns %, Jan to Jun")
fig.tight_layout()
plt.savefig("dual_axis_revenue_returns.png", dpi=150)
plt.show()

# -------------------------
# Task 4: Interpretation (association, not causation)
# -------------------------
print(
    "Between January and June, revenue rose from 200 to 340 while the returns "
    "rate drifted down from 4.5% to 3.2%, so the two series moved in opposite "
    "directions over this period."
)
print(
    "This chart shows only an association: it cannot tell us whether higher "
    "sales reduced returns, or whether something else (such as product quality "
    "or customer mix) influenced both, and six months of data is too short to "
    "draw firm conclusions."
)