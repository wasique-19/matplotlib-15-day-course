import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

# -------------------------
# Simulate all datasets
# -------------------------

# 1. Monthly expenses
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
expenses = [1850, 2100, 1750, 2300, 1950, 2200]

# 2. Expenses by category
categories = ["Rent", "Food", "Transport", "Entertainment"]
cat_expenses = [900, 450, 220, 180]

# 3. Daily spending amounts (histogram)
daily_spending = np.random.normal(65, 20, 100)
daily_spending = daily_spending[daily_spending > 0]   # drop unrealistic negatives

# -------------------------
# Build the dashboard
# -------------------------
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# (1) Line chart: monthly expenses
axes[0, 0].plot(months, expenses, marker="o", color="steelblue", linewidth=2)
axes[0, 0].set_title("Monthly Expenses")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Expenses ($)")
axes[0, 0].grid(True, linestyle="--", alpha=0.5)

# (2) Bar chart: expenses by category
axes[0, 1].bar(categories, cat_expenses, color="darkorange")
axes[0, 1].set_title("Expenses by Category")
axes[0, 1].set_xlabel("Category")
axes[0, 1].set_ylabel("Expenses ($)")
axes[0, 1].tick_params(axis="x", rotation=10)

# (3) Histogram: daily spending
axes[1, 0].hist(daily_spending, bins=15, color="mediumseagreen", edgecolor="black")
axes[1, 0].set_title("Distribution of Daily Spending")
axes[1, 0].set_xlabel("Spending ($)")
axes[1, 0].set_ylabel("Frequency")

# (4) Pie chart: expense category share
axes[1, 1].pie(cat_expenses, labels=categories, autopct="%1.1f%%",
               colors=["steelblue", "orange", "seagreen", "purple"])
axes[1, 1].set_title("Expense Category Share")

# -------------------------
# Overall title, layout, save
# -------------------------
fig.suptitle("Personal Finance Dashboard", fontsize=16, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.96])   # leave room at top for suptitle

plt.savefig("finance_dashboard.png", dpi=150)   # save BEFORE show
plt.show()