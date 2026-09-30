import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --- Chart 1: Grouped bar chart of product sales ---
df = pd.DataFrame({
    "Product": ["Product A", "Product B", "Product C", "Product D", "Product E"],
    "Last_Month": [220, 180, 310, 150, 275],
    "This_Month": [245, 200, 290, 175, 300],
})

x = np.arange(len(df["Product"]))
width = 0.35

plt.figure(figsize=(9, 5))
plt.bar(x - width/2, df["Last_Month"], width, label="Last Month", color="steelblue")
plt.bar(x + width/2, df["This_Month"], width, label="This Month", color="tomato")

plt.title("Monthly Sales Comparison by Product")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.xticks(x, df["Product"])
plt.legend()
plt.grid(True, axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()

plt.savefig("product_sales.png", dpi=150)   # save BEFORE show
plt.show()

# --- Chart 2: Histogram of customer ages ---
np.random.seed(42)
ages = np.random.normal(35, 10, 200)   # mean=35, std=10, n=200

plt.figure(figsize=(8, 5))
plt.hist(ages, bins=15, color="mediumseagreen", edgecolor="black")
plt.title("Distribution of Customer Ages (n=200)")
plt.xlabel("Age (years)")
plt.ylabel("Number of Customers")
plt.grid(True, axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()

plt.savefig("customer_ages.png", dpi=150)
plt.show()