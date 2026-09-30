import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --- Chart 1: Histogram of satisfaction scores ---
np.random.seed(42)   # for reproducible results
satisfaction_scores = np.random.randint(1, 11, 150)   # 150 scores, 1 to 10

plt.figure(figsize=(8, 5))
plt.hist(satisfaction_scores, bins=10, range=(1, 11), color="cornflowerblue", edgecolor="black")
plt.title("Distribution of Customer Satisfaction Scores (n=150)")
plt.xlabel("Satisfaction Score (1-10)")
plt.ylabel("Number of Customers")
plt.xticks(range(1, 11))
plt.grid(True, axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

# --- Chart 2: Grouped bar chart of average score per store ---
store_df = pd.DataFrame({
    "Store": ["Downtown", "Mall", "Airport"],
    "Avg_Score": [7.8, 7.1, 6.5],
})

plt.figure(figsize=(7, 5))
plt.bar(store_df["Store"], store_df["Avg_Score"], color=["steelblue", "orange", "seagreen"])
plt.title("Average Satisfaction Score by Store Location")
plt.xlabel("Store Location")
plt.ylabel("Average Score (1-10)")
plt.ylim(0, 10)
plt.grid(True, axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()