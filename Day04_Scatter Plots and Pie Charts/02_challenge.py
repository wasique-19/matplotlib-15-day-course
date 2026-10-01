import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
n = 50

# --- Build the simulated dataset ---
categories = ["Electronics", "Clothing", "Groceries", "Books"]

df = pd.DataFrame({
    "Price": np.random.uniform(10, 200, n),
    "Rating": np.random.uniform(1, 5, n),
    "UnitsSold": np.random.randint(50, 2000, n),
    "Category": np.random.choice(categories, n),
})

df["Revenue"] = df["Price"] * df["UnitsSold"]

# --- Chart 1: Bubble chart (Price vs Rating, size + color = UnitsSold) ---
plt.figure(figsize=(9, 6))
bubble = plt.scatter(
    df["Price"], df["Rating"],
    s=df["UnitsSold"] / 5,          # scale raw units down to a readable bubble size
    c=df["UnitsSold"],
    cmap="plasma",
    alpha=0.7,
    edgecolor="black",
)
plt.title("Product Price vs Rating (Bubble Size & Color = Units Sold)")
plt.xlabel("Price ($)")
plt.ylabel("Rating (1-5)")
plt.colorbar(bubble, label="Units Sold")
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()

# --- Chart 2: Pie chart of total revenue by category ---
revenue_by_category = df.groupby("Category")["Revenue"].sum()

plt.figure(figsize=(7, 7))
plt.pie(
    revenue_by_category,
    labels=revenue_by_category.index,
    autopct="%1.1f%%",
    colors=["steelblue", "orange", "seagreen", "purple"],
)
plt.title("Total Revenue Share by Category")
plt.show()