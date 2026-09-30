import matplotlib.pyplot as plt

classes = ["Class A", "Class B", "Class C", "Class D"]
students = [28, 32, 25, 30]

plt.bar(classes, students, color="steelblue")
plt.title("Number of Students per Class")
plt.xlabel("Class")
plt.ylabel("Number of Students")
plt.grid(True, axis="y", linestyle="--", alpha=0.6)
plt.show()


import matplotlib.pyplot as plt

countries = ["India", "USA", "Brazil", "Nigeria", "Japan"]
population_millions = [1428, 335, 216, 223, 124]

plt.barh(countries, population_millions, color="darkorange")
plt.title("Population by Country (Made-Up Estimates)")
plt.xlabel("Population (millions)")
plt.ylabel("Country")
plt.grid(True, axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

quarters = ["Q1", "Q2", "Q3", "Q4"]
product_a = [120, 135, 150, 170]
product_b = [110, 140, 130, 160]

x = np.arange(len(quarters))   # base positions: 0,1,2,3
width = 0.35                   # bar width

plt.bar(x - width/2, product_a, width, label="Product A", color="royalblue")
plt.bar(x + width/2, product_b, width, label="Product B", color="tomato")

plt.title("Quarterly Sales: Product A vs Product B")
plt.xlabel("Quarter")
plt.ylabel("Sales (units)")
plt.xticks(x, quarters)
plt.legend()
plt.grid(True, axis="y", linestyle="--", alpha=0.6)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(loc=0, scale=1, size=300)   # mean=0, std=1

plt.hist(data, bins=20, color="mediumseagreen", edgecolor="black")
plt.title("Histogram of 300 Random Normal Values")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True, axis="y", linestyle="--", alpha=0.6)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

regions = ["North", "South", "East", "West"]
electronics = [50, 40, 35, 45]
clothing = [30, 35, 25, 20]
groceries = [20, 25, 30, 15]

x = np.arange(len(regions))

plt.bar(x, electronics, label="Electronics", color="steelblue")
plt.bar(x, clothing, bottom=electronics, label="Clothing", color="orange")
# stack groceries on top of electronics + clothing
bottom_combined = np.array(electronics) + np.array(clothing)
plt.bar(x, groceries, bottom=bottom_combined, label="Groceries", color="seagreen")

plt.title("Revenue by Product Category and Region")
plt.xlabel("Region")
plt.ylabel("Revenue ($ thousands)")
plt.xticks(x, regions)
plt.legend()
plt.grid(True, axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()