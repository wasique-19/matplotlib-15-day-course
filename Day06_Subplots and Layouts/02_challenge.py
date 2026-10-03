import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

# -------------------------
# Simulate all datasets
# -------------------------

# 1. Monthly revenue
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [42000, 45500, 41000, 48000, 52000, 55000]

# 2. Revenue by category
categories = ["Electronics", "Clothing", "Groceries", "Books"]
cat_revenue = [120000, 85000, 95000, 40000]

# 3. Customer segments
segments = ["New", "Returning", "VIP"]
segment_counts = [220, 340, 90]

# 4. Order values (for histogram)
order_values = np.random.normal(75, 25, 300)
order_values = order_values[order_values > 0]   # drop unrealistic negatives

# 5. Price vs Rating
price = np.random.uniform(10, 200, 50)
rating = np.random.uniform(2.5, 5.0, 50)

# 6. Top 5 products
products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
product_sales = [1200, 980, 870, 760, 640]

# -------------------------
# Build the dashboard
# -------------------------
fig, axes = plt.subplots(2, 3, figsize=(16, 9))

# (1) Line chart: monthly revenue
axes[0, 0].plot(months, revenue, marker="o", color="steelblue", linewidth=2)
axes[0, 0].set_title("Monthly Revenue")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Revenue ($)")
axes[0, 0].grid(True, linestyle="--", alpha=0.5)

# (2) Bar chart: revenue by category
axes[0, 1].bar(categories, cat_revenue, color="darkorange")
axes[0, 1].set_title("Revenue by Category")
axes[0, 1].set_xlabel("Category")
axes[0, 1].set_ylabel("Revenue ($)")


# (3) Pie chart: customer segments
axes[0, 2].pie(segment_counts, labels=segments, autopct="%1.1f%%",
               colors=["steelblue", "seagreen", "gold"])
axes[0, 2].set_title("Customer Segments")

# (4) Histogram: order values
axes[1, 0].hist(order_values, bins=20, color="mediumseagreen", edgecolor="black")
axes[1, 0].set_title("Distribution of Order Values")
axes[1, 0].set_xlabel("Order Value ($)")
axes[1, 0].set_ylabel("Frequency")

# (5) Scatter: price vs rating
axes[1, 1].scatter(price, rating, color="tomato", alpha=0.7, edgecolor="black")
axes[1, 1].set_title("Price vs Rating")
axes[1, 1].set_xlabel("Price ($)")
axes[1, 1].set_ylabel("Rating")
axes[1, 1].grid(True, linestyle="--", alpha=0.4)

# (6) Horizontal bar chart: top 5 products
axes[1, 2].barh(products, product_sales, color="purple")
axes[1, 2].set_title("Top 5 Products by Units Sold")
axes[1, 2].set_xlabel("Units Sold")
axes[1, 2].invert_yaxis()   # highest-selling product on top

# -------------------------
# Overall title and layout
# -------------------------
fig.suptitle("Company Sales Dashboard", fontsize=18, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.96])   # leave room at top for suptitle
plt.show()