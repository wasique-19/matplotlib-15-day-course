import pandas as pd
import matplotlib.pyplot as plt

# 1. Build the data (replace with your own hours)
df = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Study_Hours": [2.0, 2.5, 3.0, 2.0, 1.5, 4.5, 3.5],
})

# 2. Line chart, 9 x 4 inches
plt.figure(figsize=(9, 4))
plt.plot(df["Day"], df["Study_Hours"])
plt.title("Daily Study Hours (Mon to Sun)")
plt.xlabel("Day of the Week")
plt.ylabel("Study Time (hours)")
plt.grid(True)

# 3. Save BEFORE showing
plt.savefig("study_hours.png")
plt.show()

# 4. Day with the highest study hours
top_day = df.loc[df["Study_Hours"].idxmax(), "Day"]
top_hours = df["Study_Hours"].max()
print(f"You studied the most on {top_day}, with {top_hours} hours.")