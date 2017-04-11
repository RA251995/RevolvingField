import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure(facecolor="white")
ax = plt.axes(aspect=1, xlim=(-175, 175), ylim=(-175, 175), frameon=False, xticks=[], yticks=[])
r_line, = ax.plot([], [], lw=2, color="red")
y_line, = ax.plot([], [], lw=2, color="yellow")
b_line, = ax.plot([], [], lw=2, color="blue")
sum_line, = ax.plot([], [], lw=2.5, color="green")

x1 = np.array([0, 0])
y1 = np.array([0, 100])
x2 = np.array([0, -100*np.cos(np.pi/6)])
y2 = np.array([0, -100*np.sin(np.pi/6)])
x3 = np.array([0, 100*np.cos(np.pi/6)])
y3 = np.array([0, -100*np.sin(np.pi/6)])

ax.plot(x1, y1, color='#cccccc')
ax.plot(x2, y2, color='#cccccc')
ax.plot(x3, y3, color='#cccccc')
circ= plt.Circle((0, 0), radius=150, color='#cccccc', fill=False)
ax.add_patch(circ)

def init():
    r_line.set_data([], [])
    y_line.set_data([], [])
    b_line.set_data([], [])
    sum_line.set_data([], [])
    return r_line, y_line, b_line, sum_line,

locus_x = np.array([])
locus_y = np.array([])

def animate(i):
    theta = i*np.pi/180
    rx = np.array([0.0, 0.0])
    ry = np.array([0.0, 100.0*np.sin(theta)])
    r_line.set_data(rx, ry)
    yx = np.array([0.0, -100*np.cos(np.pi/6)*np.sin(theta-2*np.pi/3)])
    yy = np.array([0.0, -100*np.sin(np.pi/6)*np.sin(theta-2*np.pi/3)])
    y_line.set_data(yx, yy)
    bx = np.array([0.0, 100.0*np.cos(np.pi/6)*np.sin(theta-4*np.pi/3)])
    by = np.array([0.0, -100.0*np.sin(np.pi/6)*np.sin(theta-4*np.pi/3)])
    b_line.set_data(bx, by)
    sum_x = np.array([0.0, rx[1]+yx[1]+bx[1]])
    sum_y = np.array([0.0, ry[1]+yy[1]+by[1]])
    sum_line.set_data(sum_x, sum_y)
    return r_line, y_line, b_line, sum_line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=360, interval=20, blit=True)

plt.show()
