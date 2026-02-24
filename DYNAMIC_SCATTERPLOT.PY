import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

x_data = []
y_data = []

scatter = ax.scatter(x_data, y_data)

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

def update(frame):
    x_data.append(np.random.rand() * 10)
    y_data.append(np.random.rand() * 10)
    scatter.set_offsets(np.c_[x_data, y_data])
    return scatter,

ani = FuncAnimation(fig, update, frames=20, interval=500)

plt.show()
