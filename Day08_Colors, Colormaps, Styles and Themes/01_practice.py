import matplotlib.pyplot as plt

classes = ["Class A", "Class B", "Class C", "Class D"]
students = [28, 32, 25, 30]

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

axes[0].bar(classes, students, color="steelblue")       # named color
axes[0].set_title("Named Color")

axes[1].bar(classes, students, color="#4C72B0")          # hex code
axes[1].set_title("Hex Code")

axes[2].bar(classes, students, color=(0.3, 0.45, 0.7))   # RGB tuple (0-1 scale)
axes[2].set_title("RGB Tuple")

plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Default style
fig, ax = plt.subplots()
ax.plot(x, y, marker="o")
ax.set_title("Default Style")
plt.show()

# ggplot style
plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.plot(x, y, marker="o")
ax.set_title("ggplot Style")
plt.show()


import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
height = np.random.uniform(150, 200, 50)
weight = np.random.uniform(50, 100, 50)
age = np.random.uniform(18, 70, 50)   # naturally low-to-high

fig, ax = plt.subplots(figsize=(8, 6))
scatter = ax.scatter(height, weight, c=age, cmap="viridis", edgecolor="black")
ax.set_title("Height vs Weight (Color = Age)")
ax.set_xlabel("Height (cm)")
ax.set_ylabel("Weight (kg)")
fig.colorbar(scatter, label="Age (years)")
plt.show()


import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.random.uniform(0, 100, 50)
y = np.random.uniform(0, 100, 50)
temp_change = np.random.uniform(-5, 5, 50)   # centered at zero

fig, ax = plt.subplots(figsize=(8, 6))
scatter = ax.scatter(x, y, c=temp_change, cmap="coolwarm", vmin=-5, vmax=5, edgecolor="black")
ax.set_title("Temperature Change from Baseline")
ax.set_xlabel("x")
ax.set_ylabel("y")
fig.colorbar(scatter, label="Temp Change (°C)")
plt.show()


import matplotlib.pyplot as plt

# Custom 3-color theme
PRIMARY = "#2E5984"     # deep blue
SECONDARY = "#D98E04"   # warm orange
ACCENT = "#5A8F5A"      # muted green

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Line chart
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 120, 115, 140, 135]
axes[0].plot(months, sales, marker="o", color=PRIMARY, linewidth=2)
axes[0].set_title("Monthly Sales")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("Sales")
axes[0].grid(True, color=ACCENT, linestyle="--", alpha=0.3)

# Bar chart
categories = ["A", "B", "C"]
values = [45, 30, 25]
axes[1].bar(categories, values, color=[PRIMARY, SECONDARY, ACCENT])
axes[1].set_title("Category Totals")
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Value")

# Pie chart
axes[2].pie(values, labels=categories, autopct="%1.1f%%",
            colors=[PRIMARY, SECONDARY, ACCENT])
axes[2].set_title("Category Share")

plt.tight_layout()
plt.show()