import matplotlib.pyplot as plt
import random

data = [random.randint(1, 100) for _ in range(1000)]

plt.hist(data, bins=20)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Static Histogram")
plt.show()