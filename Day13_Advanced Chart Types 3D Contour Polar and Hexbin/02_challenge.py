import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# -------------------------
# Shared grid for the surface and contour panels
# -------------------------
x = np.linspace(-np.pi, np.pi, 150)
y = np.linspace(-np.pi, np.pi, 150)
X, Y = np.meshgrid(x, y)
Z = np.cos(X) * np.sin(Y)

fig = plt.figure(figsize=(14, 11))

# -------------------------
# Top-left: 3D surface
# -------------------------
ax1 = fig.add_subplot(2, 2, 1, projection="3d")
surf = ax1.plot_surface(X, Y, Z, cmap="viridis", edgecolor="none")
ax1.set_title("3D Surface: cos(X) · sin(Y)")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")

# -------------------------
# Top-right: filled contour of the same data
# -------------------------
ax2 = fig.add_subplot(2, 2, 2)
cf = ax2.contourf(X, Y, Z, levels=20, cmap="viridis")
ax2.set_title("Filled Contour of the Same Data")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_aspect("equal")
fig.colorbar(cf, ax=ax2, label="Z value")

# -------------------------
# Bottom-left: polar plot
# -------------------------
ax3 = fig.add_subplot(2, 2, 3, projection="polar")
theta = np.linspace(0, 2 * np.pi, 500)
r = 1 + np.sin(3 * theta)
ax3.plot(theta, r, color="crimson", linewidth=2)
ax3.fill(theta, r, color="crimson", alpha=0.2)
ax3.set_title("Polar Plot: r = 1 + sin(3θ)", pad=20)

# -------------------------
# Bottom-right: hexbin of 4,000 random points
# -------------------------
ax4 = fig.add_subplot(2, 2, 4)
hx = np.random.normal(0, 1, 4000)
hy = np.random.normal(0, 1, 4000)
hb = ax4.hexbin(hx, hy, gridsize=30, cmap="YlOrRd", mincnt=1)
ax4.set_title("Hexbin of 4,000 Random Points")
ax4.set_xlabel("x")
ax4.set_ylabel("y")
fig.colorbar(hb, ax=ax4, label="Points per hexagon")

# -------------------------
# Figure title and layout
# -------------------------
fig.suptitle("Advanced Gallery", fontsize=18, fontweight="bold")
fig.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()