import matplotlib.pyplot as plt

sizes = list(map(int, input("Enter values separated by space: ").split()))
labels = input("Enter labels separated by space: ").split()

colors = plt.cm.Paired(range(len(sizes)))
explode = [0.05] * len(sizes)

plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()
30