import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# -------------------------
# Data
# -------------------------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [420, 455, 410, 480, 520, 550, 530, 575, 600, 640, 690, 760]   # $ thousands
profit_margin = [11.5, 12.0, 10.8, 12.5, 13.2, 13.8, 13.0, 14.1, 14.5, 14.0, 15.2, 16.0]  # %

categories = ["Electronics", "Clothing", "Groceries", "Books", "Home"]
category_revenue = [2400, 1500, 1800, 600, 1100]

# Colour coding
BAR_COLOR = "#2E5984"    # revenue (left axis)
LINE_COLOR = "#D9534F"   # profit margin (right axis)
PIE_COLORS = ["#2E5984", "#D98E04", "#5A8F5A", "#8E6BBF", "#7F7F7F"]

# -------------------------
# Figure with two Axes (1 x 2)
# -------------------------
fig, (ax1, ax_pie) = plt.subplots(1, 2, figsize=(16, 6),
                                  gridspec_kw={"width_ratios": [2, 1]})

# ----- Left: dual-axis chart -----
ax1.bar(months, revenue, color=BAR_COLOR, alpha=0.85, label="Revenue ($K)")
ax1.set_xlabel("Month")
ax1.set_ylabel("Revenue ($ thousands)", color=BAR_COLOR)
ax1.tick_params(axis="y", labelcolor=BAR_COLOR)
ax1.set_title("Monthly Revenue vs Profit Margin")
ax1.grid(True, axis="y", linestyle="--", alpha=0.4)

ax2 = ax1.twinx()   # second y-axis sharing the same x-axis
ax2.plot(months, profit_margin, color=LINE_COLOR, marker="o",
         linewidth=2.5, label="Profit Margin (%)")
ax2.set_ylabel("Profit Margin (%)", color=LINE_COLOR)
ax2.tick_params(axis="y", labelcolor=LINE_COLOR)
ax2.set_ylim(0, 20)
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:.0f}%"))

# Colour the axis spines to match their series
ax1.spines["left"].set_color(BAR_COLOR)
ax2.spines["right"].set_color(LINE_COLOR)

# Merged legend (handles from BOTH axes in one box)
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left")

# ----- Right: pie chart -----
ax_pie.pie(category_revenue, labels=categories, colors=PIE_COLORS,
           autopct="%1.1f%%", startangle=90, pctdistance=0.8,
           wedgeprops={"edgecolor": "white", "linewidth": 1.5},
           textprops={"fontsize": 10})
ax_pie.set_title("Revenue Share by Category")

# ----- Figure-level title and layout -----
fig.suptitle("Executive Snapshot", fontsize=18, fontweight="bold")
fig.tight_layout(rect=[0, 0, 1, 0.94])   # reserve room for the suptitle
plt.show()