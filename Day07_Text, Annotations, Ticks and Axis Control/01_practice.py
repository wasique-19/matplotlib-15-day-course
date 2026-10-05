import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(x, y, marker="o", color="steelblue")
ax.set_title("Line Chart with Text Label")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.text(3, 20, "Rapid growth here", fontsize=10, color="darkred")
ax.grid(True)
plt.show()


import matplotlib.pyplot as plt

classes = ["Introduction to Python", "Data Structures", "Web Development", "Machine Learning"]
students = [28, 32, 25, 30]

fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(classes, students, color="steelblue")
ax.set_title("Number of Students per Course")
ax.set_xlabel("Course")
ax.set_ylabel("Number of Students")
ax.set_xticklabels(classes, rotation=45, ha="right")   # ha = horizontal alignment
plt.tight_layout()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 50)
y = (x - 5) ** 2 + 3   # a simple parabola with a clear minimum

fig, ax = plt.subplots()
ax.plot(x, y, color="steelblue")
ax.set_title("Line Chart with Minimum Point Annotated")
ax.set_xlabel("x")
ax.set_ylabel("y")

min_idx = np.argmin(y)
min_x, min_y = x[min_idx], y[min_idx]

ax.annotate(
    f"Min: {min_y:.2f}",
    xy=(min_x, min_y),              # point being annotated
    xytext=(min_x + 1.5, min_y + 5),  # where the text sits
    arrowprops=dict(facecolor="black", arrowstyle="->"),
)
ax.grid(True)
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

months = ["Jan", "Feb", "Mar", "Apr", "May"]
completion_rate = [0.65, 0.72, 0.68, 0.80, 0.85]   # values as fractions

fig, ax = plt.subplots()
ax.plot(months, completion_rate, marker="o", color="seagreen")
ax.set_title("Monthly Completion Rate")
ax.set_xlabel("Month")
ax.set_ylabel("Completion Rate")
ax.yaxis.set_major_formatter(PercentFormatter(xmax=1.0))   # 0.65 -> "65%"
ax.grid(True)
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [42000, 45500, 38000, 48000, 52000, 39500]

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(months, revenue, marker="o", color="steelblue", linewidth=2)
ax.set_title("Monthly Revenue with Max/Min Annotated")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue")

# Custom currency formatter for the y-axis
def currency_formatter(value, pos):
    return f"${value:,.0f}"

ax.yaxis.set_major_formatter(FuncFormatter(currency_formatter))

# Annotate the maximum
max_idx = np.argmax(revenue)
ax.annotate(
    f"Max: ${revenue[max_idx]:,}",
    xy=(months[max_idx], revenue[max_idx]),
    xytext=(max_idx - 1.3, revenue[max_idx] + 3000),
    arrowprops=dict(facecolor="green", arrowstyle="->"),
)

# Annotate the minimum
min_idx = np.argmin(revenue)
ax.annotate(
    f"Min: ${revenue[min_idx]:,}",
    xy=(months[min_idx], revenue[min_idx]),
    xytext=(min_idx - 1.3, revenue[min_idx] - 5000),
    arrowprops=dict(facecolor="red", arrowstyle="->"),
)

ax.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()