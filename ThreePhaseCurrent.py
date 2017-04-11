import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure(facecolor="white")
ax = plt.axes(aspect=1, xlim=(0, 2*np.pi), ylim=(-1.5, 1.5), frameon=False, xticks=[], yticks=[])

x = np.arange(0, 2*np.pi, 0.01)
r_line, = ax.plot(x, np.sin(x), color="red")
y_line, = ax.plot(x, np.sin(x-2*np.pi/3), color="yellow")
b_line, = ax.plot(x, np.sin(x-4*np.pi/3), color ="blue")

def animate(i):
    # update the data
    theta = i*np.pi/180
    r_line.set_ydata(np.sin(x + theta))
    y_line.set_ydata(np.sin(x - 2*np.pi/3 + theta))
    b_line.set_ydata(np.sin(x - 4*np.pi/3 + theta))
    return r_line, y_line, b_line,


# Init only required for blitting to give a clean slate.
def init():
    r_line.set_ydata(np.ma.array(x, mask=True))
    y_line.set_ydata(np.ma.array(x, mask=True))
    b_line.set_ydata(np.ma.array(x, mask=True))
    return r_line, y_line, b_line,

ani = animation.FuncAnimation(fig, animate, 360, init_func=init,
                              interval=10, blit=True)
plt.show()