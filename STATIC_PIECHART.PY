import matplotlib.pyplot as plt

sizes = [25, 35, 20, 20]
labels = ['A', 'B', 'C', 'D']
colors = ['gold', 'lightblue', 'lightgreen', 'pink']
explode = (0.1, 0, 0, 0)

plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()
