import pandas as pd
import matplotlib.pyplot as plt

# 1. Build the data
df = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Steps": [7200, 8400, 6900, 9100, 7600, 10500, 8800],
})

goal = 8000

# 2. Build the chart
plt.figure(figsize=(9, 5))
plt.plot(df["Day"], df["Steps"], marker="o", linestyle="-", color="blue", linewidth=2, label="Actual Steps")
plt.axhline(y=goal, linestyle="--", color="red", linewidth=2, label="Daily Goal (8,000)")

plt.title("Weekly Steps vs Daily Goal")
plt.xlabel("Day of the Week")
plt.ylabel("Steps")
plt.xticks(range(len(df["Day"])), df["Day"])
plt.ylim(6000, 11000)   # comfortably fits both series
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()

# 3. Save the chart
plt.savefig("steps_vs_goal.png", dpi=150)
plt.show()