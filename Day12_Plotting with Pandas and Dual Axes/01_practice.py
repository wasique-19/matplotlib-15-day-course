import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Steps": [7200, 8400, 6900, 9100, 7600],
})

ax = df.plot(x="Day", y="Steps", marker="o", figsize=(8, 4),
             title="Daily Steps", legend=False)
ax.set_xlabel("Day")
ax.set_ylabel("Steps")
ax.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Steps": [7200, 8400, 6900, 9100, 7600],
})

ax = df.plot.barh(x="Day", y="Steps", color="steelblue", figsize=(8, 4),
                  title="Daily Steps", legend=False)
ax.set_xlabel("Steps")
ax.set_ylabel("Day")
ax.invert_yaxis()   # Monday at the top
plt.tight_layout()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

sales = pd.DataFrame({
    "Region": ["North", "South", "East", "West", "North", "South", "East", "West"],
    "Revenue": [12000, 9500, 15000, 7000, 8000, 11000, 6000, 9000],
})

totals = sales.groupby("Region")["Revenue"].sum().sort_values(ascending=False)

ax = totals.plot.bar(color="darkorange", figsize=(8, 5),
                     title="Total Revenue by Region")
ax.set_xlabel("Region")
ax.set_ylabel("Revenue ($)")
ax.tick_params(axis="x", rotation=0)
ax.grid(True, axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
dates = pd.date_range("2025-01-01", periods=30, freq="D")
df = pd.DataFrame({
    "Visits": np.random.normal(500, 50, 30),
    "Signups": np.random.normal(60, 10, 30),
    "Sales": np.random.normal(25, 6, 30),
    "Returns": np.random.normal(3, 1, 30),
}, index=dates)

axes = df.plot(subplots=True, layout=(2, 2), sharex=True,
               figsize=(11, 7), marker=".", legend=False)

for ax, col in zip(axes.flat, df.columns):
    ax.set_title(col)
    ax.grid(True, linestyle="--", alpha=0.5)

plt.suptitle("Four Metrics Over 30 Days", fontsize=14, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Units_Sold": [1200, 1350, 1100, 1500, 1650, 1580],
    "Return_Rate": [4.2, 3.8, 5.1, 3.5, 3.0, 3.3],   # percent
})

BAR_COLOR = "steelblue"
LINE_COLOR = "crimson"

fig, ax1 = plt.subplots(figsize=(10, 5))

# Left axis: bars
bars = ax1.bar(df["Month"], df["Units_Sold"], color=BAR_COLOR, alpha=0.8,
               label="Units Sold")
ax1.set_xlabel("Month")
ax1.set_ylabel("Units Sold", color=BAR_COLOR)
ax1.tick_params(axis="y", labelcolor=BAR_COLOR)

# Right axis: line (twinx shares the same x-axis)
ax2 = ax1.twinx()
line, = ax2.plot(df["Month"], df["Return_Rate"], color=LINE_COLOR, marker="o",
                 linewidth=2.5, label="Return Rate (%)")
ax2.set_ylabel("Return Rate (%)", color=LINE_COLOR)
ax2.tick_params(axis="y", labelcolor=LINE_COLOR)
ax2.set_ylim(0, 8)

# One merged legend
ax1.legend([bars, line], ["Units Sold", "Return Rate (%)"], loc="upper left")

ax1.set_title("Units Sold vs Return Rate")
ax1.grid(True, axis="y", linestyle="--", alpha=0.4)
fig.tight_layout()
plt.show()