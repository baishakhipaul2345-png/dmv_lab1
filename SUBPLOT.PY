import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x)

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot data in each subplot
axs[0, 0].plot(x, y1)
axs[0, 0].set_title("Sine")

axs[0, 1].plot(x, y2)
axs[0, 1].set_title("Cosine")

axs[1, 0].plot(x, y3)
axs[1, 0].set_title("Tangent")

axs[1, 1].plot(x, y4)
axs[1, 1].set_title("Exponential")

# Adjust layout
plt.tight_layout()
plt.show()
