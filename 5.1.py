import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [12000, 15000, 17000, 14000, 18000, 22000]
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(months, sales, color='blue', marker='o')
plt.title("Monthly Sales Trend")
plt.subplot(1, 2, 2)
plt.bar(months, sales, color='yellow')
plt.show()
