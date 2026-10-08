import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

np.random.seed(42)

# -------------------------
# Simulate 100 days of sign-ups
# -------------------------
dates = pd.date_range("2025-01-01", periods=100, freq="D")
base = np.linspace(80, 110, 100)                  # gentle upward trend
signups = base + np.random.normal(0, 10, 100)     # daily noise

# Deliberate spike: 10-day referral campaign
campaign_start = pd.Timestamp("2025-02-15")
campaign_end = pd.Timestamp("2025-02-24")         # 10 days inclusive
mask = (dates >= campaign_start) & (dates <= campaign_end)
signups[mask] += 60

signups = np.clip(signups, 0, None).astype(int)

s = pd.Series(signups, index=dates)
rolling = s.rolling(window=7).mean()

# -------------------------
# Build the chart
# -------------------------
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(s.index, s.values, color="lightsteelblue", linewidth=1, label="Daily sign-ups")
ax.plot(rolling.index, rolling.values, color="darkblue", linewidth=2.5, label="7-day rolling average")
ax.axvspan(campaign_start, campaign_end + pd.Timedelta(days=1),
           color="gold", alpha=0.3, label="Referral campaign (10 days)")

ax.set_title("Daily Website Sign-ups with Rolling Average and Campaign Period")
ax.set_xlabel("Date")
ax.set_ylabel("Sign-ups per Day")

# Month + day formatting, one tick every 2 weeks
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO, interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))

ax.legend(loc="upper left")
ax.grid(True, linestyle="--", alpha=0.5)
fig.autofmt_xdate()
plt.tight_layout()

plt.savefig("signups_trend.png", dpi=150)   # save BEFORE show
plt.show()