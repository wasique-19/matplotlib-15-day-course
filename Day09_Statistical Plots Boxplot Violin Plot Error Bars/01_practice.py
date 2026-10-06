import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
scores = np.random.normal(70, 12, 100)

fig, ax = plt.subplots(figsize=(6, 6))
ax.boxplot(scores, vert=True)
ax.set_title("Box Plot of Exam Scores")
ax.set_ylabel("Score")
ax.set_xticklabels(["Exam Scores"])
plt.show()


import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
group_a = np.random.normal(70, 8, 100)
group_b = np.random.normal(80, 5, 100)
group_c = np.random.normal(60, 15, 100)

fig, ax = plt.subplots(figsize=(8, 6))
ax.boxplot([group_a, group_b, group_c], tick_labels=["Group A", "Group B", "Group C"])
ax.set_title("Score Distribution by Group")
ax.set_ylabel("Score")
ax.grid(True, axis="y", linestyle="--", alpha=0.5)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
group_a = np.random.normal(70, 8, 100)
group_b = np.random.normal(80, 5, 100)
group_c = np.random.normal(60, 15, 100)

fig, ax = plt.subplots(figsize=(8, 6))
ax.violinplot([group_a, group_b, group_c], showmedians=True)
ax.set_title("Score Distribution by Group (Violin Plot)")
ax.set_ylabel("Score")
ax.set_xticks([1, 2, 3])
ax.set_xticklabels(["Group A", "Group B", "Group C"])
ax.grid(True, axis="y", linestyle="--", alpha=0.5)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

categories = ["Category A", "Category B", "Category C", "Category D"]
averages = [72, 85, 68, 79]
std_devs = [5, 3, 8, 4]

fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(categories, averages, yerr=std_devs, capsize=6, color="steelblue", alpha=0.8)
ax.set_title("Average Values with Standard Deviation")
ax.set_xlabel("Category")
ax.set_ylabel("Average Value")
ax.grid(True, axis="y", linestyle="--", alpha=0.5)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Bimodal distribution: two merged normal distributions
cluster_1 = np.random.normal(50, 5, 150)
cluster_2 = np.random.normal(80, 5, 150)
bimodal_data = np.concatenate([cluster_1, cluster_2])

# Regular (unimodal) normal distribution
normal_data = np.random.normal(65, 10, 300)

fig, ax = plt.subplots(figsize=(8, 6))
ax.violinplot([normal_data, bimodal_data], showmedians=True)
ax.set_title("Unimodal vs Bimodal Distribution")
ax.set_ylabel("Value")
ax.set_xticks([1, 2])
ax.set_xticklabels(["Normal (Unimodal)", "Merged Clusters (Bimodal)"])
ax.grid(True, axis="y", linestyle="--", alpha=0.5)

# Comment: A box plot would summarize the bimodal data with a single median
# and a single box spanning roughly 50 to 80 — it would look like one wide,
# evenly-spread group. It has no way to show that the data is actually two
# distinct clusters near 50 and 80 with a gap between them. The violin plot's
# width directly traces the data's density, so it visibly shows two separate
# "bulges" for the bimodal distribution, revealing the hidden two-group
# structure that summary statistics alone would mask.
plt.show()