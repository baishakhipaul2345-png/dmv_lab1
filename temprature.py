import matplotlib.pyplot as plt

weights = [25, 28, 29, 30, 34, 35, 35, 37, 38]

plt.figure()  
plt.boxplot(weights)

plt.xlabel("Weights (grams)")
plt.title("Box Plot of Weights")

plt.show()