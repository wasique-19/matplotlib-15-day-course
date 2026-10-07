import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [42000, 45500, 41000, 48000, 52000, 55000]

fig, ax = plt.subplots(figsize=(9, 5))
ax.fill_between(months, revenue, color="steelblue", alpha=0.4)
ax.plot(months, revenue, color="steelblue", linewidth=2)
ax.set_title("Monthly Revenue (Filled Area)")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue ($)")
ax.grid(True, linestyle="--", alpha=0.5)
plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
df = pd.DataFrame({
    "A": np.random.normal(50, 10, 100),
    "B": np.random.normal(30, 5, 100),
    "C": np.random.normal(70, 15, 100),
})
df["B"] = df["A"] * 0.5 + np.random.normal(0, 3, 100)   # correlate B with A

corr = df.corr()

fig, ax = plt.subplots(figsize=(6, 5))
im = ax.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
ax.set_title("Correlation Heatmap")
ax.set_xticks(range(len(corr.columns)))
ax.set_yticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns)
ax.set_yticklabels(corr.columns)
fig.colorbar(im, label="Correlation")
plt.show()


import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
electronics = [20, 22, 19, 25, 28, 30]
clothing = [15, 17, 16, 18, 20, 19]
groceries = [10, 11, 12, 10, 13, 14]

fig, ax = plt.subplots(figsize=(9, 5))
ax.stackplot(months, electronics, clothing, groceries,
             labels=["Electronics", "Clothing", "Groceries"],
             colors=["steelblue", "orange", "seagreen"], alpha=0.8)
ax.set_title("Stacked Revenue by Category Over 6 Months")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue ($ thousands)")
ax.legend(loc="upper left")
plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
df = pd.DataFrame({
    "A": np.random.normal(50, 10, 100),
    "B": np.random.normal(30, 5, 100),
    "C": np.random.normal(70, 15, 100),
})
df["B"] = df["A"] * 0.5 + np.random.normal(0, 3, 100)

corr = df.corr()

fig, ax = plt.subplots(figsize=(6, 5))
im = ax.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
ax.set_title("Correlation Heatmap with Values")
ax.set_xticks(range(len(corr.columns)))
ax.set_yticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns)
ax.set_yticklabels(corr.columns)

# Annotate each cell with its value
for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        ax.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center", color="black")

fig.colorbar(im, label="Correlation")
plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

# Simulate raw sales records
regions = ["North", "South", "East", "West"]
months = ["Jan", "Feb", "Mar", "Apr"]

records = []
for region in regions:
    for month in months:
        records.append({"Region": region, "Month": month,
                         "Sales": np.random.randint(50, 200)})
df = pd.DataFrame(records)

# Build the pivot table
pivot = df.pivot_table(values="Sales", index="Region", columns="Month")
pivot = pivot[months]   # ensure column order is Jan, Feb, Mar, Apr

fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(pivot, cmap="YlGnBu")
ax.set_title("Sales by Region and Month")
ax.set_xlabel("Month")
ax.set_ylabel("Region")
ax.set_xticks(range(len(pivot.columns)))
ax.set_yticks(range(len(pivot.index)))
ax.set_xticklabels(pivot.columns)
ax.set_yticklabels(pivot.index)

for i in range(len(pivot.index)):
    for j in range(len(pivot.columns)):
        ax.text(j, i, f"{pivot.iloc[i, j]:.0f}", ha="center", va="center", color="black")

fig.colorbar(im, label="Sales (units)")
plt.tight_layout()
plt.show()