import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [200, 240, 180, 300, 250],
    'Product': ['X', 'Y', 'X', 'Z', 'Y'],
    'Price': [150, 200, 170, 220, 180],
    'Income': [5000, 6000, 5500, 6200, 5800],
    'Spending': [3000, 3200, 3100, 3500, 3300]
}

df = pd.DataFrame(data)

plt.plot(df['Month'], df['Sales'], 'r--')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()
plt.show()

df['Product'].value_counts().plot(kind='bar', color='purple')
plt.title("Product Count")
plt.xlabel("Product")
plt.ylabel("Count")
plt.grid()
plt.show()

plt.hist(df['Price'], bins=20, color='green')
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.grid()
plt.show()

plt.scatter(df['Income'], df['Spending'], color='blue')
plt.title("Income vs Spending")
plt.xlabel("Income")
plt.ylabel("Spending")
plt.grid()
plt.show()
