import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, np.sin(x), color="steelblue", linewidth=2)
ax.set_title("Sine Wave")
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")

fig.savefig("chart.png", dpi=200, bbox_inches="tight")
plt.show()


import os
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, np.sin(x), color="steelblue", linewidth=2)
ax.set_title("Sine Wave")
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")

for fmt in ["png", "pdf", "svg"]:
    filename = f"chart.{fmt}"
    fig.savefig(filename, dpi=200, bbox_inches="tight")
    print(f"{filename}: {os.path.getsize(filename) / 1024:.1f} KB")
plt.show()


import matplotlib.pyplot as plt

plt.rcParams.update({
    "axes.spines.top": False,
    "axes.spines.right": False,
    "font.size": 12,
    "axes.grid": True,
    "grid.color": "#CCCCCC",
    "grid.alpha": 0.5,
    "grid.linestyle": "--",
})

categories = ["A", "B", "C", "D"]
values = [28, 32, 25, 30]

fig, ax = plt.subplots(figsize=(7, 5))
ax.bar(categories, values, color="steelblue")
ax.set_axisbelow(True)   # draw the grid behind the bars
ax.set_title("Bar Chart with Custom rcParams")
ax.set_xlabel("Category")
ax.set_ylabel("Value")
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Okabe-Ito colour-blind-safe palette (four of its eight colours)
ORANGE = "#E69F00"
SKY_BLUE = "#56B4E9"
GREEN = "#009E73"
VERMILLION = "#D55E00"

x = np.arange(1, 9)
series = {
    "Series 1": (x * 1.0, ORANGE, "o"),
    "Series 2": (x * 1.5, SKY_BLUE, "s"),
    "Series 3": (x * 2.0, GREEN, "^"),
    "Series 4": (x * 2.5, VERMILLION, "D"),
}

fig, ax = plt.subplots(figsize=(8, 5))
for name, (y, color, marker) in series.items():
    ax.plot(x, y, color=color, marker=marker, markersize=7, linewidth=2, label=name)

ax.set_title("Four Lines with the Okabe-Ito Palette")
ax.set_xlabel("x")
ax.set_ylabel("Value")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()


import os
import numpy as np
import matplotlib.pyplot as plt

def export_chart(fig, name, formats=("png", "pdf"), dpi=300):
    """Save a figure in several formats inside a 'figures' folder, then close it."""
    os.makedirs("figures", exist_ok=True)
    saved = []
    for fmt in formats:
        path = os.path.join("figures", f"{name}.{fmt}")
        fig.savefig(path, dpi=dpi, bbox_inches="tight")
        saved.append(path)
    plt.close(fig)
    print("Saved:", ", ".join(saved))

# Example use
x = np.linspace(0, 10, 100)
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, np.cos(x), color="darkorange", linewidth=2)
ax.set_title("Cosine Wave")
ax.set_xlabel("x")
ax.set_ylabel("cos(x)")

export_chart(fig, "cosine_wave", formats=("png", "pdf", "svg"))