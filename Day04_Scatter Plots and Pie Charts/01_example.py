import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.linspace(0, 10, 30)
noise = np.random.normal(0, 1, 30)
y = x + noise

plt.scatter(x, y, color="steelblue")
plt.title("Scatter Plot: x vs x + Noise")
plt.xlabel("x")
plt.ylabel("x + noise")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()


import matplotlib.pyplot as plt

categories = ["Electronics", "Clothing", "Groceries", "Books"]
values = [35, 25, 30, 10]

plt.pie(values, labels=categories, autopct="%1.1f%%", colors=["steelblue", "orange", "seagreen", "purple"])
plt.title("Sales Share by Category")
plt.show()


import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.random.uniform(0, 100, 50)
y = np.random.uniform(0, 100, 50)
colors = np.random.uniform(0, 50, 50)   # third variable, e.g. temperature

scatter = plt.scatter(x, y, c=colors, cmap="viridis")
plt.title("Scatter Plot with Color-Encoded Third Variable")
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar(scatter, label="Value of Third Variable")
plt.grid(True, linestyle="--", alpha=0.4)
plt.show()


import matplotlib.pyplot as plt

categories = ["Electronics", "Clothing", "Groceries", "Books"]
values = [35, 25, 30, 10]
explode = [0.1, 0, 0, 0]   # pull out the largest slice (Electronics)

plt.pie(values, labels=categories, autopct="%1.1f%%", explode=explode,
        colors=["steelblue", "orange", "seagreen", "purple"])
plt.title("Sales Share by Category (Largest Highlighted)")
plt.show()


import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n = 25
price = np.random.uniform(10, 200, n)         # x: product price
rating = np.random.uniform(2.5, 5.0, n)        # y: customer rating
units_sold = np.random.uniform(50, 2000, n)    # size: units sold

plt.figure(figsize=(9, 6))
plt.scatter(price, rating, s=units_sold / 5, alpha=0.6, color="coral", edgecolor="black")
plt.title("Product Price vs Rating (Bubble Size = Units Sold)")
plt.xlabel("Price ($)")
plt.ylabel("Customer Rating")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()