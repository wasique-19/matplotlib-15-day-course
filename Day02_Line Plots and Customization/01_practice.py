import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
plt.plot(x, x, label="y = x")
plt.plot(x, 2 * x, label="y = 2x")
plt.title("Two Lines on One Chart")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
plt.plot(x, x, label="y = x", color="purple")
plt.plot(x, 2 * x, label="y = 2x", linestyle="--")
plt.title("Custom Color and Linestyle")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()


import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temps = [18, 20, 19, 22, 25, 27, 24]

plt.plot(range(len(days)), temps, marker="o", color="orangered")
plt.title("Weekly Temperatures")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.xticks(range(len(days)), days)   # custom tick labels
plt.grid(True)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

plt.plot(x, y, color="teal")
plt.title("Sine Wave with Fixed Y-Axis Range")
plt.xlabel("x (radians)")
plt.ylabel("sin(x)")
plt.ylim(-1.5, 1.5)
plt.grid(True)
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
actual = [105, 112, 98, 120, 130, 128]
target = [100, 110, 110, 115, 120, 125]
last_year = [95, 100, 90, 108, 115, 118]

plt.figure(figsize=(9, 5))
plt.plot(months, actual, marker="o", color="steelblue", linewidth=2, label="Actual")
plt.plot(months, target, marker="s", color="darkorange", linewidth=2, label="Target")
plt.plot(months, last_year, linestyle="--", color="gray", linewidth=2, label="Last Year's Actuals")

plt.title("Actual vs Target vs Last Year (6 Months)")
plt.xlabel("Month")
plt.ylabel("Sales (units)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()