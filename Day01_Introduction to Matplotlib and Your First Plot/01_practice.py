import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.title("Squares of Numbers")
plt.xlabel("Number")
plt.ylabel("Square")
plt.show()


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.figure(figsize=(10, 4))   # width, height in inches
plt.plot(x, y)
plt.title("Squares of Numbers")
plt.xlabel("Number")
plt.ylabel("Square")
plt.grid(True)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 200)
y = np.cos(x)

plt.plot(x, y)
plt.title("One Cosine Wave")
plt.xlabel("x (radians)")
plt.ylabel("cos(x)")
plt.grid(True)
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Visitors": [120, 135, 150, 145, 170, 210, 190],
})

df.plot(x="Day", y="Visitors", marker="o", title="Daily Website Visitors")
plt.ylabel("Visitors")
plt.savefig("visitors.png")   # save BEFORE show()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
y = x ** 2

# Comment: matplotlib draws straight line segments between consecutive points.
# With 200 points the segments are so short that the eye sees a smooth curve;
# with only 5 points each segment is long, so the corners between them show.
plt.plot(x, y)
plt.title("y = x²")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()