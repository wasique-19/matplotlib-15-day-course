import pandas as pd
import matplotlib.pyplot as plt

# 1. Build the data
df = pd.DataFrame({
    "Week": [f"Week {i}" for i in range(1, 9)],
    "Weight_kg": [82.5, 81.9, 81.2, 81.5, 80.4, 79.8, 79.1, 78.6],
})

# 2. Total change = last week minus first week
total_change = df["Weight_kg"].iloc[-1] - df["Weight_kg"].iloc[0]

# 3. Build a clean, labeled line chart
plt.figure(figsize=(9, 5))
plt.plot(df["Week"], df["Weight_kg"])
plt.title("Weekly Weight Progress Over 8 Weeks")
plt.xlabel("Week")
plt.ylabel("Weight (kg)")
plt.grid(True)

# 4. Save BEFORE showing, otherwise the PNG may come out blank
plt.savefig("weight_trend.png")
plt.show()

# 5. One sentence stating the trend
if total_change < 0:
    trend = "down"
elif total_change > 0:
    trend = "up"
else:
    trend = "flat"

print(f"The weight trend is {trend}, with a total change of {total_change:+.1f} kg over 8 weeks.")