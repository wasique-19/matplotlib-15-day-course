"""Day 13 - Mini Assignment: Delivery Performance Explorer"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10)

# -------------------------
# 1. Simulate 3,000 deliveries
# -------------------------
n = 3000
distance_km = np.clip(np.random.normal(8, 3, n), 1, None)
time_min = distance_km * 4 + np.random.normal(0, 4, n)   # roughly 4 min per km, plus noise

# -------------------------
# 2. Hexbin of distance vs delivery time (+ colorbar, trend line, legend)
# -------------------------
fig1, ax1 = plt.subplots(figsize=(9, 6))
hb = ax1.hexbin(distance_km, time_min, gridsize=35, cmap="YlOrRd", mincnt=1)
fig1.colorbar(hb, ax=ax1, label="Deliveries per hexagon")

slope, intercept = np.polyfit(distance_km, time_min, 1)
line_x = np.linspace(distance_km.min(), distance_km.max(), 100)
ax1.plot(line_x, slope * line_x + intercept, color="navy", linewidth=2,
         label=f"Trend: {slope:.1f} min per km")

ax1.set_title("Delivery Time vs Distance (3,000 Deliveries)")
ax1.set_xlabel("Distance (km)")
ax1.set_ylabel("Delivery Time (minutes)")
ax1.legend(loc="upper left")
fig1.tight_layout()
fig1.savefig("delivery_hexbin.png", dpi=150)
plt.show()

# -------------------------
# 3 & 4. Radar chart: two delivery partners across five metrics
# All metrics are scored 0-10 where HIGHER IS BETTER
# (cost is shown as "Cost Efficiency", returns as "Low Returns")
# -------------------------
metrics = ["Speed", "Accuracy", "Rating", "Cost Efficiency", "Low Returns"]
partners = {
    "Partner A": [8.5, 7.0, 8.0, 5.5, 7.5],
    "Partner B": [6.0, 9.0, 7.5, 8.0, 8.5],
}
colors = ["#2E5984", "#D98E04"]

angles = np.linspace(0, 2 * np.pi, len(metrics), endpoint=False).tolist()
angles += angles[:1]   # close the shape

fig2, ax2 = plt.subplots(figsize=(8, 8), subplot_kw={"projection": "polar"})
for (name, values), color in zip(partners.items(), colors):
    vals = values + values[:1]
    ax2.plot(angles, vals, color=color, linewidth=2, label=name)
    ax2.fill(angles, vals, color=color, alpha=0.15)

ax2.set_xticks(angles[:-1])
ax2.set_xticklabels(metrics, fontsize=11)
ax2.set_ylim(0, 10)
ax2.set_title("Delivery Partner Comparison (0-10, higher is better)", pad=25, fontsize=13)
ax2.legend(loc="upper right", bbox_to_anchor=(1.25, 1.1))
fig2.tight_layout()
fig2.savefig("delivery_radar.png", dpi=150)
plt.show()

# -------------------------
# 5. Interpretation
# -------------------------
print(
    "The hexbin chart reveals its pattern better, because with 3,000 deliveries "
    "it shows both the clear upward relationship between distance and time and "
    "where most deliveries cluster, which a scatter plot of this many points "
    "would hide."
)
print(
    "The radar chart is good for comparing the overall profiles of the two "
    "partners (A is faster, B is more accurate and cost-efficient), but it "
    "summarises each partner in five scores, so it cannot reveal a relationship "
    "or a distribution the way the hexbin does."
)