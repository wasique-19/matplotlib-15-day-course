import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
n = 100

# -------------------------
# Chart 1: Correlation heatmap of 4 business metrics
# -------------------------
marketing_spend = np.random.normal(3000, 500, n)

# Sign-ups scale with marketing spend (deliberate strong correlation), plus noise
signups = marketing_spend * 0.8 + np.random.normal(0, 400, n)

# Support tickets: mostly independent noise, weak relation to signups
support_tickets = np.random.normal(50, 15, n) + signups * 0.01

# Churn rate: independent of the others
churn_rate = np.random.normal(5, 1.5, n)

df = pd.DataFrame({
    "Marketing_Spend": marketing_spend,
    "Signups": signups,
    "Support_Tickets": support_tickets,
    "Churn_Rate": churn_rate,
})

corr = df.corr()

fig, ax = plt.subplots(figsize=(7, 6))
im = ax.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)

ax.set_title("Correlation Heatmap of Business Metrics")
ax.set_xticks(range(len(corr.columns)))
ax.set_yticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=45, ha="right")
ax.set_yticklabels(corr.columns)

for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        ax.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center", color="black")

fig.colorbar(im, label="Correlation Coefficient")
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=150)   # save before show
plt.show()

# -------------------------
# Chart 2: Stacked area plot of 3 product categories
# -------------------------
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
electronics = [20, 22, 19, 25, 28, 30]
clothing = [15, 17, 16, 18, 20, 19]
groceries = [10, 11, 12, 10, 13, 14]

fig2, ax2 = plt.subplots(figsize=(9, 5))
ax2.stackplot(months, electronics, clothing, groceries,
              labels=["Electronics", "Clothing", "Groceries"],
              colors=["steelblue", "orange", "seagreen"], alpha=0.8)
ax2.set_title("Stacked Revenue by Category Over 6 Months")
ax2.set_xlabel("Month")
ax2.set_ylabel("Revenue ($ thousands)")
ax2.legend(loc="upper left")
plt.tight_layout()

plt.savefig("stacked_revenue.png", dpi=150)
plt.show()