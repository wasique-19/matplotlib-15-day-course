import matplotlib.pyplot as plt

# -------------------------
# Apply style BEFORE plotting
# -------------------------
plt.style.use("seaborn-v0_8-whitegrid")

# -------------------------
# Custom brand colors, defined once
# -------------------------
BRAND_PRIMARY = "#1F4E79"    # deep navy blue
BRAND_SECONDARY = "#E8A33D"  # warm gold

# -------------------------
# Datasets (constructed manually)
# -------------------------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [42000, 45500, 41000, 48000, 52000, 55000]

categories = ["Electronics", "Clothing", "Groceries", "Books"]
cat_revenue = [120000, 85000, 95000, 40000]

# -------------------------
# Build the 2-panel figure
# -------------------------
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Left: line chart
axes[0].plot(months, revenue, marker="o", color=BRAND_PRIMARY, linewidth=2.5)
axes[0].set_title("Monthly Revenue")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("Revenue ($)")

# Right: bar chart (alternating between the two brand colors)
bar_colors = [BRAND_PRIMARY, BRAND_SECONDARY, BRAND_PRIMARY, BRAND_SECONDARY]
axes[1].bar(categories, cat_revenue, color=bar_colors)
axes[1].set_title("Revenue by Category")
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Revenue ($)")
axes[1].tick_params(axis="x", rotation=15)

# -------------------------
# Overall title and layout
# -------------------------
fig.suptitle("Q2 Revenue Report", fontsize=16, fontweight="bold", color=BRAND_PRIMARY)
plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.show()