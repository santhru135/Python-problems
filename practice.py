import matplotlib.pyplot as plt

# First subplot (left side)
plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st plot
plt.plot([1, 2, 3, 4], [10, 20, 25, 30], label='Line 1',marker = "o") 
plt.plot([1, 2, 3, 4], [30, 25, 20, 15], label='Line 2',marker = "o") 
plt.xticks([1, 2, 3, 4])
plt.yticks([10, 20, 30], rotation=90)
plt.xlabel('X Axis Label', fontsize=14, color="blue")
plt.ylabel('Y Axis Label', fontsize=14, color="red")
plt.annotate("Plot1 Lable",xy = (3,30),fontsize = 14,color = "green")
plt.title("Line Plot 1")
plt.legend(loc="upper left")
plt.annotate("This Plot",xy = (2,20),xytext = (2.5,20),arrowprops=dict(facecolor = "black",arrowstyle = "->"))
plt.grid(True)

# Second subplot (right side)
plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd plot
plt.plot([1, 2, 3, 4], [5, 15, 10, 20], label='Line A') 
plt.plot([1, 2, 3, 4], [25, 20, 15, 10], label='Line B') 
plt.xticks([1, 2, 3, 4], ['One', 'Two', 'Three', 'Four'])
plt.yticks([10, 20, 30], ['Low', 'Medium', 'High'], rotation=90)
plt.xlabel('X Axis Label', fontsize=14, color="blue")
plt.ylabel('Y Axis Label', fontsize=14, color="red")
plt.title("Line Plot 2")
plt.legend(loc="upper left")
plt.grid(True)
# Adjust layout and display
plt.tight_layout()
plt.show()
