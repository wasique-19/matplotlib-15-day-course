import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(11, 4))

# Left: line chart
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
axes[0].plot(x, y, marker="o", color="steelblue")
axes[0].set_title("Line Chart")
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")
axes[0].grid(True)

# Right: bar chart
classes = ["A", "B", "C", "D"]
students = [28, 32, 25, 30]
axes[1].bar(classes, students, color="orange")
axes[1].set_title("Bar Chart")
axes[1].set_xlabel("Class")
axes[1].set_ylabel("Students")

plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt

def build_2x2():
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    for i, ax in enumerate(axes.flat):
        ax.plot([1, 2, 3], [1, 4, 9])
        ax.set_title(f"Subplot {i+1} with a Longer Title Here")
        ax.set_xlabel("x-axis label")
        ax.set_ylabel("y-axis label")
    return fig

# Without tight_layout — titles/labels may overlap neighboring subplots
build_2x2()
plt.show()

# With tight_layout — spacing automatically adjusted
build_2x2()
plt.tight_layout()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
fig, axes = plt.subplots(2, 2, figsize=(11, 9))

# Top-left: histogram
data = np.random.normal(0, 1, 300)
axes[0, 0].hist(data, bins=20, color="mediumseagreen", edgecolor="black")
axes[0, 0].set_title("Histogram")

# Top-right: scatter plot
x = np.random.uniform(0, 10, 50)
y = x + np.random.normal(0, 1, 50)
axes[0, 1].scatter(x, y, color="steelblue")
axes[0, 1].set_title("Scatter Plot")

# Bottom-left: pie chart
axes[1, 0].pie([35, 25, 30, 10], labels=["A", "B", "C", "D"], autopct="%1.1f%%")
axes[1, 0].set_title("Pie Chart")

# Bottom-right: line chart
months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 120, 115, 140]
axes[1, 1].plot(months, sales, marker="o", color="tomato")
axes[1, 1].set_title("Line Chart")

plt.tight_layout()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
product_a = [100, 110, 105, 120, 130, 128]
product_b = [95, 100, 98, 115, 120, 125]

fig, axes = plt.subplots(2, 1, figsize=(8, 8), sharex=True, sharey=True)

axes[0].plot(months, product_a, marker="o", color="steelblue")
axes[0].set_title("Product A Sales")
axes[0].set_ylabel("Units Sold")
axes[0].grid(True, linestyle="--", alpha=0.5)

axes[1].plot(months, product_b, marker="o", color="tomato")
axes[1].set_title("Product B Sales")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Units Sold")
axes[1].grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

datasets = {
    "Normal (mean=0)": np.random.normal(0, 1, 300),
    "Uniform (0 to 10)": np.random.uniform(0, 10, 300),
    "Exponential": np.random.exponential(2, 300),
    "Poisson (lambda=4)": np.random.poisson(4, 300),
}

fig, axes = plt.subplots(2, 2, figsize=(11, 9))

for ax, (title, data) in zip(axes.flat, datasets.items()):
    ax.hist(data, bins=20, color="cornflowerblue", edgecolor="black")
    ax.set_title(title)
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")

plt.tight_layout()
plt.show()