import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
n = 40

# --- Build the simulated dataset ---
df = pd.DataFrame({
    "SquareFeet": np.random.uniform(600, 4000, n),
    "Bedrooms": np.random.randint(1, 7, n),   # 1 to 6 bedrooms
})
# Price loosely tied to size and bedrooms, plus some noise, to look realistic
df["Price"] = (df["SquareFeet"] * 150 + df["Bedrooms"] * 10000
                + np.random.normal(0, 20000, n))

# --- Chart 1: Scatter plot (SquareFeet vs Price, size & color = Bedrooms) ---
plt.figure(figsize=(9, 6))
scatter = plt.scatter(
    df["SquareFeet"], df["Price"],
    s=df["Bedrooms"] * 40,       # scale bedrooms into a readable bubble size
    c=df["Bedrooms"],
    cmap="cool",
    alpha=0.7,
    edgecolor="black",
)
plt.title("House Price vs Square Footage (Size & Color = Bedrooms)")
plt.xlabel("Square Feet")
plt.ylabel("Price ($)")
plt.colorbar(scatter, label="Bedrooms")
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()

# --- Chart 2: Pie chart by bedroom category ---
def bedroom_group(b):
    if b <= 2:
        return "1-2 Bedrooms"
    elif b <= 4:
        return "3-4 Bedrooms"
    else:
        return "5+ Bedrooms"

df["Bedroom_Group"] = df["Bedrooms"].apply(bedroom_group)
group_counts = df["Bedroom_Group"].value_counts()

# Explode the largest group
explode = [0.1 if group == group_counts.idxmax() else 0 for group in group_counts.index]

plt.figure(figsize=(7, 7))
plt.pie(
    group_counts,
    labels=group_counts.index,
    autopct="%1.1f%%",
    explode=explode,
    colors=["steelblue", "orange", "seagreen"],
)
plt.title("Proportion of Houses by Bedroom Count")
plt.show()