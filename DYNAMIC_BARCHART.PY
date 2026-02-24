import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

categories = ['A', 'B', 'C', 'D', 'E']
values = [random.randint(1, 10) for _ in categories]

fig, ax = plt.subplots()
bars = ax.bar(categories, values)

ax.set_ylim(0, 20)

def update(frame):
    new_values = [random.randint(1, 20) for _ in categories]
    for bar, val in zip(bars, new_values):
        bar.set_height(val)
    return bars

ani = animation.FuncAnimation(fig, update, frames=50, interval=500)

plt.show()