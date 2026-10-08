import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

np.random.seed(42)

# -------------------------
# Simulate 180 days of app downloads
# -------------------------
dates = pd.date_range("2025-01-01", periods=180, freq="D")
base = np.linspace(500, 700, 180)                  # gentle upward trend
downloads = base + np.random.normal(0, 50, 180)    # daily noise

# Deliberate spike: 10-day app-store featuring
feature_start = pd.Timestamp("2025-04-10")
feature_end = pd.Timestamp("2025-04-19")           # 10 days inclusive
mask = (dates >= feature_start) & (dates <= feature_end)
downloads[mask] += 400

downloads = np.clip(downloads, 0, None).astype(int)

s = pd.Series(downloads, index=dates)
rolling = s.rolling(window=14).mean()

# -------------------------
# Build the chart
# -------------------------
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(s.index, s.values, color="lightsteelblue", linewidth=1, label="Daily downloads")
ax.plot(rolling.index, rolling.values, color="darkblue", linewidth=2.5, label="14-day rolling average")
ax.axvspan(feature_start, feature_end + pd.Timedelta(days=1),
           color="gold", alpha=0.3, label="App-store featuring (10 days)")

ax.set_title("Daily App Downloads with Rolling Average and Featured Period")
ax.set_xlabel("Date")
ax.set_ylabel("Downloads per Day")

# Month + year formatting
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))

ax.legend(loc="upper left")
ax.grid(True, linestyle="--", alpha=0.5)
fig.autofmt_xdate()          # rotates tick labels so they don't collide
plt.tight_layout()
plt.show()