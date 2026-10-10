import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
y = np.zeros_like(x)
z = x ** 2

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection="3d")
ax.plot(x, y, z, color="steelblue", linewidth=2)
ax.set_title("3D Line: z = x²")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()


import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 4 * np.pi, 400)
r = theta

fig, ax = plt.subplots(figsize=(7, 7), subplot_kw={"projection": "polar"})
ax.plot(theta, r, color="crimson", linewidth=2)
ax.set_title("Polar Plot: r = θ", pad=20)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 200)
y = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(x, y)
Z = X ** 2 + Y ** 2

fig, ax = plt.subplots(figsize=(8, 6))
cf = ax.contourf(X, Y, Z, levels=20, cmap="viridis")
ax.set_title("Filled Contour of Z = X² + Y²")
ax.set_xlabel("X")
ax.set_ylabel("Y")
fig.colorbar(cf, label="Z value")
ax.set_aspect("equal")
plt.show()


import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.random.normal(0, 1, 3000)
y = np.random.normal(0, 1, 3000)

fig, axes = plt.subplots(1, 2, figsize=(13, 6))

# Left: hexbin
hb = axes[0].hexbin(x, y, gridsize=30, cmap="YlOrRd", mincnt=1)
axes[0].set_title("Hexbin (3,000 points)")
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")
fig.colorbar(hb, ax=axes[0], label="Points per hexagon")

# Right: scatter
axes[1].scatter(x, y, s=5, alpha=0.4, color="steelblue")
axes[1].set_title("Scatter (3,000 points)")
axes[1].set_xlabel("x")
axes[1].set_ylabel("y")

plt.tight_layout()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

categories = ["Quality", "Price", "Design", "Support", "Durability"]
products = {
    "Product A": [4.5, 3.0, 4.0, 3.5, 4.2],
    "Product B": [3.5, 4.5, 3.0, 4.0, 3.2],
    "Product C": [4.0, 3.8, 4.5, 2.8, 3.9],
}
colors = ["#2E5984", "#D98E04", "#5A8F5A"]

n = len(categories)
angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
angles += angles[:1]   # close the shape by repeating the first angle

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={"projection": "polar"})

for (name, values), color in zip(products.items(), colors):
    vals = values + values[:1]   # close the shape by repeating the first value
    ax.plot(angles, vals, color=color, linewidth=2, label=name)
    ax.fill(angles, vals, color=color, alpha=0.15)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=11)
ax.set_ylim(0, 5)
ax.set_title("Product Ratings Across Five Categories", pad=25, fontsize=14)
ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.1))
plt.tight_layout()
plt.show()