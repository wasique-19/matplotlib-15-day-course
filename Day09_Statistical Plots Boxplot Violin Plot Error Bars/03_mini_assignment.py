import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# -------------------------
# Simulate exam scores for 3 classes
# -------------------------
class_names = ["Class A", "Class B", "Class C"]
means = [75, 82, 78]
stds = [12, 6, 18]

class_data = [np.random.normal(m, s, 80) for m, s in zip(means, stds)]

# -------------------------
# Build the 2-panel figure
# -------------------------
fig, axes = plt.subplots(1, 2, figsize=(13, 6))

# Left: box plot of all 3 classes
axes[0].boxplot(class_data, tick_labels=class_names)
axes[0].set_title("Exam Score Distribution by Class")
axes[0].set_ylabel("Score")
axes[0].grid(True, axis="y", linestyle="--", alpha=0.5)

# Right: error bar chart of mean ± std
sample_means = [data.mean() for data in class_data]
sample_stds = [data.std() for data in class_data]

axes[1].bar(class_names, sample_means, yerr=sample_stds, capsize=6,
            color="seagreen", alpha=0.8)
axes[1].set_title("Mean Exam Score ± Std Dev")
axes[1].set_xlabel("Class")
axes[1].set_ylabel("Score")
axes[1].grid(True, axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()

# -------------------------
# Identify highest average and most consistent
# -------------------------
highest_idx = np.argmax(sample_means)
most_consistent_idx = np.argmin(sample_stds)

print(f"{class_names[highest_idx]} has the highest average score "
      f"({sample_means[highest_idx]:.1f}).")

if highest_idx == most_consistent_idx:
    print(f"{class_names[most_consistent_idx]} is also the most consistent class, "
          f"the same class with the highest average.")
else:
    print(f"{class_names[most_consistent_idx]} is the most consistent class instead "
          f"(lowest std dev of {sample_stds[most_consistent_idx]:.1f}), "
          f"different from the class with the highest average.")