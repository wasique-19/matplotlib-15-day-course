import pandas as pd
import matplotlib.pyplot as plt

def plot_sales_trend(ax, df, product_name):
    """Draws a fully labeled monthly sales line chart for a given product, onto a given ax."""
    ax.plot(df["Month"], df["Sales"], marker="o", linestyle="-", color="steelblue", linewidth=2)
    ax.set_title(f"Monthly Sales Trend: {product_name}")
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales (units)")
    ax.grid(True, linestyle="--", alpha=0.6)

# --- Dataset 1: Product X ---
df_x = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [150, 165, 140, 180, 200, 210],
})

# --- Dataset 2: Product Y ---
df_y = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [90, 95, 100, 85, 110, 130],
})

# --- Figure 1: Product X ---
fig1, ax1 = plt.subplots(figsize=(8, 5))
plot_sales_trend(ax1, df_x, "Product X")
plt.tight_layout()
plt.show()

# --- Figure 2: Product Y ---
fig2, ax2 = plt.subplots(figsize=(8, 5))
plot_sales_trend(ax2, df_y, "Product Y")
plt.tight_layout()
plt.show()