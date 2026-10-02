import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(x, y)
ax.set_title("Squares of Numbers")
ax.set_xlabel("Number")
ax.set_ylabel("Square")
ax.grid(True)
plt.show()


import matplotlib.pyplot as plt

classes = ["Class A", "Class B", "Class C", "Class D"]
students = [28, 32, 25, 30]

fig, ax = plt.subplots()
ax.bar(classes, students, color="steelblue")
ax.set_title("Number of Students per Class")
ax.set_xlabel("Class")
ax.set_ylabel("Number of Students")
ax.grid(True, axis="y", linestyle="--", alpha=0.6)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(ax, data, title):
    ax.hist(data, bins=15, color="mediumseagreen", edgecolor="black")
    ax.set_title(title)
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.grid(True, axis="y", linestyle="--", alpha=0.6)

np.random.seed(42)
ages = np.random.normal(35, 10, 200)

fig, ax = plt.subplots()
plot_histogram(ax, ages, "Distribution of Customer Ages")
plt.show()


import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x1 = np.random.normal(5, 1, 30)
y1 = np.random.normal(5, 1, 30)
x2 = np.random.normal(8, 1, 30)
y2 = np.random.normal(8, 1, 30)

fig, ax = plt.subplots()
ax.scatter(x1, y1, color="steelblue", label="Group A")
ax.scatter(x2, y2, color="tomato", label="Group B")
ax.set_title("Scatter Plot of Two Groups")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.4)
plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_grouped_bar(df, value_col, group_col, ax):
    """Draws a fully labeled bar chart of value_col, grouped/averaged by group_col."""
    grouped = df.groupby(group_col)[value_col].mean()
    ax.bar(grouped.index.astype(str), grouped.values, color="steelblue")
    ax.set_title(f"Average {value_col} by {group_col}")
    ax.set_xlabel(group_col)
    ax.set_ylabel(f"Average {value_col}")
    ax.grid(True, axis="y", linestyle="--", alpha=0.6)

# Dataset 1: student scores by class
df1 = pd.DataFrame({
    "Class": ["A", "A", "B", "B", "C", "C"],
    "Score": [72, 78, 65, 70, 88, 84],
})

# Dataset 2: house prices by bedroom count
df2 = pd.DataFrame({
    "Bedrooms": [2, 2, 3, 3, 4, 4],
    "Price": [200000, 215000, 260000, 275000, 320000, 310000],
})

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
plot_grouped_bar(df1, "Score", "Class", axes[0])
plot_grouped_bar(df2, "Price", "Bedrooms", axes[1])
plt.tight_layout()
plt.show()