import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# -------------------------
# Simulate 4 servers' response times (ms)
# -------------------------
server_names = ["Server A", "Server B", "Server C", "Server D"]
means = [120, 95, 110, 98]
stds = [15, 8, 25, 5]

server_data = [np.random.normal(m, s, 80) for m, s in zip(means, stds)]

# -------------------------
# Build the 2-panel figure
# -------------------------
fig, axes = plt.subplots(1, 2, figsize=(13, 6))

# Left: box plot of all 4 distributions
axes[0].boxplot(server_data, tick_labels=server_names)
axes[0].set_title("Response Time Distribution by Server")
axes[0].set_ylabel("Response Time (ms)")
axes[0].grid(True, axis="y", linestyle="--", alpha=0.5)

# Right: error bar chart of mean ± std
sample_means = [data.mean() for data in server_data]
sample_stds = [data.std() for data in server_data]

axes[1].bar(server_names, sample_means, yerr=sample_stds, capsize=6,
            color="steelblue", alpha=0.8)
axes[1].set_title("Mean Response Time ± Std Dev")
axes[1].set_xlabel("Server")
axes[1].set_ylabel("Response Time (ms)")
axes[1].grid(True, axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()

# -------------------------
# Identify fastest and most consistent
# -------------------------
fastest_idx = np.argmin(sample_means)
most_consistent_idx = np.argmin(sample_stds)

print(f"{server_names[fastest_idx]} is fastest on average, "
      f"with a mean response time of {sample_means[fastest_idx]:.1f} ms.")

if fastest_idx == most_consistent_idx:
    print(f"{server_names[most_consistent_idx]} is also the most consistent, "
          f"with the lowest standard deviation ({sample_stds[most_consistent_idx]:.1f} ms).")
else:
    print(f"{server_names[most_consistent_idx]} is the most consistent instead, "
          f"with the lowest standard deviation ({sample_stds[most_consistent_idx]:.1f} ms), "
          f"meaning the fastest server and the most reliable server are different.")