import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

circle = plt.Circle((0, 5), 0.3)
ax.add_patch(circle)

x = np.linspace(0, 10, 200)

def update(frame):
    circle.center = (x[frame], 5)
    return circle,

ani = animation.FuncAnimation(fig, update, frames=len(x), interval=30)

plt.show()
