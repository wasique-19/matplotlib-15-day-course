import pandas as pd
import matplotlib.pyplot as plt

# 1. Build the data
df = pd.DataFrame({
    "Exam": [1, 2, 3, 4, 5],
    "ClassA_Avg": [72, 75, 78, 80, 84],
    "ClassB_Avg": [68, 74, 73, 79, 81],
})

# 2. Custom x-axis labels
exam_labels = [f"Exam {n}" for n in df["Exam"]]

# 3. Build the comparison chart
plt.figure(figsize=(9, 5))
plt.plot(df["Exam"], df["ClassA_Avg"], marker="o", linestyle="-", color="blue", linewidth=2, label="Class A")
plt.plot(df["Exam"], df["ClassB_Avg"], marker="s", linestyle="--", color="orange", linewidth=2, label="Class B")

plt.title("Class A vs Class B: Average Test Scores")
plt.xlabel("Exam")
plt.ylabel("Average Score")
plt.xticks(df["Exam"], exam_labels)   # replace 1,2,3... with "Exam 1", "Exam 2"...
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.show()