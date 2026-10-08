import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
dates = pd.date_range("2025-01-01", periods=60, freq="D")   # datetime64 dtype
values = np.random.normal(100, 10, 60)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(dates, values, color="steelblue", linewidth=1.5)
ax.set_title("60 Days of Simulated Daily Values")
ax.set_xlabel("Date")
ax.set_ylabel("Value")
ax.grid(True, linestyle="--", alpha=0.5)
fig.autofmt_xdate()   # auto-rotates date labels so they don't collide
plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

np.random.seed(42)
dates = pd.date_range("2025-01-01", periods=60, freq="D")
values = np.random.normal(100, 10, 60)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(dates, values, color="steelblue")
ax.set_title("Daily Values with Custom Date Format")
ax.set_xlabel("Date")
ax.set_ylabel("Value")

ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))   # e.g. "Jan 15"
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))  # one tick per week

ax.grid(True, linestyle="--", alpha=0.5)
fig.autofmt_xdate()
plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
dates = pd.date_range("2025-01-01", periods=90, freq="D")
trend = np.linspace(100, 130, 90)
values = trend + np.random.normal(0, 8, 90)

s = pd.Series(values, index=dates)
rolling = s.rolling(window=7).mean()

fig, ax = plt.subplots(figsize=(11, 5))
ax.plot(s.index, s.values, color="lightsteelblue", linewidth=1, label="Daily value")
ax.plot(rolling.index, rolling.values, color="darkblue", linewidth=2.5, label="7-day rolling average")
ax.set_title("Noisy Daily Data with 7-Day Rolling Average")
ax.set_xlabel("Date")
ax.set_ylabel("Value")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.5)
fig.autofmt_xdate()
plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
dates = pd.date_range("2025-01-01", periods=90, freq="D")
values = np.random.normal(100, 10, 90)

fig, ax = plt.subplots(figsize=(11, 5))
ax.plot(dates, values, color="steelblue", label="Daily value")

ax.axvspan(pd.Timestamp("2025-02-10"), pd.Timestamp("2025-02-24"),
           color="gold", alpha=0.3, label="Promotion period (2 weeks)")

ax.set_title("Daily Values with Highlighted Promotion Period")
ax.set_xlabel("Date")
ax.set_ylabel("Value")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.5)
fig.autofmt_xdate()
plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

np.random.seed(42)
dates = pd.date_range("2025-01-01", periods=120, freq="D")
base = np.linspace(200, 260, 120)
values = base + np.random.normal(0, 15, 120)

# Simulate a boost during the event period
event_start, event_end = pd.Timestamp("2025-03-01"), pd.Timestamp("2025-03-14")
mask = (dates >= event_start) & (dates <= event_end)
values[mask] += 40

s = pd.Series(values, index=dates)
rolling = s.rolling(window=7).mean()

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(s.index, s.values, color="lightsteelblue", linewidth=1, label="Daily sales")
ax.plot(rolling.index, rolling.values, color="darkblue", linewidth=2.5, label="7-day rolling average")
ax.axvspan(event_start, event_end, color="gold", alpha=0.3, label="Flash sale event")

ax.set_title("Daily Sales with Rolling Average and Event Highlight")
ax.set_xlabel("Date")
ax.set_ylabel("Sales (units)")

ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=mdates.MO))

ax.legend(loc="upper left")
ax.grid(True, linestyle="--", alpha=0.5)
fig.autofmt_xdate()
plt.tight_layout()
plt.show()