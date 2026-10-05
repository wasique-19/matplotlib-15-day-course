import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# Apply style BEFORE plotting
# -------------------------
plt.style.use("seaborn-v0_8-whitegrid")

# -------------------------
# Custom 3-color theme, defined once
# -------------------------
PRIMARY = "#2E5984"     # deep blue
SECONDARY = "#D98E04"   # warm orange
ACCENT = "#5A8F5A"      # muted green

# -------------------------
# Datasets
# -------------------------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
values = [320, 345, 310, 380, 400, 420]

np.random.seed(42)
x = np.random.uniform(0, 100, 50)
y = np.random.uniform(0, 100, 50)
third_var = np.random.uniform(0, 50, 50)   # e.g. a numeric variable like "experience"

# -------------------------
# Build the 1x2 figure
# -------------------------
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Left: line chart using primary color
axes[0].plot(months, values, marker="o", color=PRIMARY, linewidth=2.5)
axes[0].set_title("Monthly Values")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("Value")

# Right: scatter plot with sequential colormap + colorbar
scatter = axes[1].scatter(x, y, c=third_var, cmap="viridis", edgecolor="black")
axes[1].set_title("x vs y (Color = Third Variable)")
axes[1].set_xlabel("x")
axes[1].set_ylabel("y")
fig.colorbar(scatter, ax=axes[1], label="Third Variable")

# -------------------------
# Overall title, layout, save
# -------------------------
fig.suptitle("Themed Report", fontsize=16, fontweight="bold", color=PRIMARY)
plt.tight_layout(rect=[0, 0, 1, 0.94])

plt.savefig("themed_report.png", dpi=150)
plt.show()