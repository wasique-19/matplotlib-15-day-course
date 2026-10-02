import pandas as pd
import matplotlib.pyplot as plt

# --- Part 1: OO rewrite of the Day 1 study hours chart ---
df = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Study_Hours": [2.0, 2.5, 3.0, 2.0, 1.5, 4.5, 3.5],
})

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(df["Day"], df["Study_Hours"], marker="o", color="royalblue", linewidth=2)
ax.set_title("Daily Study Hours (Mon to Sun)")
ax.set_xlabel("Day of the Week")
ax.set_ylabel("Study Time (hours)")
ax.set_ylim(0, 6)
ax.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

# --- Part 2: Reusable function for any 7-day DataFrame ---
def plot_week(ax, data, title):
    """Draws a fully labeled 7-day line chart (Day vs value column) onto a given ax."""
    day_col = data.columns[0]
    value_col = data.columns[1]

    ax.plot(data[day_col], data[value_col], marker="o", color="royalblue", linewidth=2)
    ax.set_title(title)
    ax.set_xlabel("Day of the Week")
    ax.set_ylabel(value_col.replace("_", " "))
    ax.set_ylim(0, data[value_col].max() * 1.3)
    ax.grid(True, linestyle="--", alpha=0.6)

# Confirm it works with a new dataset: weekly water intake
water_df = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Water_Liters": [2.1, 1.8, 2.5, 2.0, 2.3, 1.5, 1.9],
})

fig2, ax2 = plt.subplots(figsize=(9, 4))
plot_week(ax2, water_df, "Daily Water Intake (Mon to Sun)")
plt.tight_layout()
plt.show()