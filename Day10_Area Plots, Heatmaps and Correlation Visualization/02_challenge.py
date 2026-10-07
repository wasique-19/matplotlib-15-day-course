import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
n = 100

# -------------------------
# Simulate 5 business metrics with deliberate correlations
# -------------------------
ad_spend = np.random.normal(5000, 1000, n)

# Website visits scale with ad spend (strong positive correlation), plus noise
website_visits = ad_spend * 2.5 + np.random.normal(0, 1500, n)

# Revenue scales with website visits (strong positive correlation), plus noise
revenue = website_visits * 3 + np.random.normal(0, 3000, n)

# Customer complaints loosely rise with revenue/traffic (weak positive), plus noise
complaints = revenue * 0.002 + np.random.normal(20, 10, n)

# Employee satisfaction: unrelated to the others, pure independent noise
employee_satisfaction = np.random.normal(7, 1.2, n)

df = pd.DataFrame({
    "Ad_Spend": ad_spend,
    "Website_Visits": website_visits,
    "Revenue": revenue,
    "Complaints": complaints,
    "Employee_Satisfaction": employee_satisfaction,
})

corr = df.corr()

# -------------------------
# Build the annotated heatmap
# -------------------------
fig, ax = plt.subplots(figsize=(8, 7))
im = ax.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)

ax.set_title("Correlation Heatmap of Business Metrics")
ax.set_xticks(range(len(corr.columns)))
ax.set_yticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=45, ha="right")
ax.set_yticklabels(corr.columns)

for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        ax.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center",
                 color="black", fontsize=9)

fig.colorbar(im, label="Correlation Coefficient")
plt.tight_layout()
plt.show()

# -------------------------
# Identify strongest relationship and unrelated metric
# -------------------------
corr_no_diag = corr.where(~np.eye(len(corr), dtype=bool))   # mask the diagonal (self-correlation = 1.0)
strongest_pair = corr_no_diag.abs().stack().idxmax()
strongest_value = corr.loc[strongest_pair[0], strongest_pair[1]]

print(f"The strongest positive relationship is between {strongest_pair[0]} and "
      f"{strongest_pair[1]} (correlation of {strongest_value:.2f}), reflecting how "
      f"website traffic and resulting revenue were built to move together.")
print("Employee_Satisfaction appears unrelated to the other four metrics, with "
      "correlations close to zero across the board, since it was simulated as "
      "independent random noise.")