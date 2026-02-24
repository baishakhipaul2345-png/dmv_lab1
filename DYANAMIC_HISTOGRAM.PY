

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

data = [random.randint(1, 100) for _ in range(100)]

fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 30)

def update(frame):
    ax.clear()
    new_data = [random.randint(1, 100) for _ in range(100)]
    ax.hist(new_data, bins=20)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 30)

ani = animation.FuncAnimation(fig, update, interval=500)

plt.show()