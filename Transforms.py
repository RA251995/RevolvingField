import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.rc('text', usetex=True)

fig = plt.figure(facecolor="white")
ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)
ax1.set_xlim(0, 2*np.pi) 
ax1.set_ylim(-1.5, 1.5)
ax2.set_xlim(0, 2*np.pi) 
ax2.set_ylim(-1.5, 1.5)
ax3.set_xlim(0, 2*np.pi) 
ax3.set_ylim(-1.5, 1.5)
ax1.set_aspect(1)
ax2.set_aspect(1)
ax3.set_aspect(1)
ax1.axis('off')
ax2.axis('off')
ax3.axis('off')

x = np.arange(0, 2*np.pi, 0.01)
r_line, = ax1.plot(x, np.sin(x), color="red", label=r'A')
y_line, = ax1.plot(x, np.sin(x-2*np.pi/3), color="yellow", label=r'B')
b_line, = ax1.plot(x, np.sin(x-4*np.pi/3), color ="blue", label=r'C')
ax1.legend(loc=5, bbox_to_anchor=(-0.1, 0.5))
ax1.set_title('3 Phase Waveform')

alpha_line, = ax2.plot(x, np.sin(x), color='red', label=r'$\alpha$-axis')
beta_line, = ax2.plot(x, 1/(3**0.5)*(np.sin(x)+2*np.sin(x-2*np.pi/3)), label=r'$\beta$-axis')
ax2.legend(loc=5, bbox_to_anchor=(-0.1, 0.5))
ax2.set_title('Clarke Transformation')

d_line, = ax3.plot(x, np.sin(x)*np.cos(x+np.pi/6)+1/(3**0.5)*(np.sin(x)+2*np.sin(x-2*np.pi/3))*np.sin(x+np.pi/6), label='d-axis')
q_line, = ax3.plot(x, np.sin(x)*-np.sin(x+np.pi/6)+1/(3**0.5)*(np.sin(x)+2*np.sin(x-2*np.pi/3))*np.cos(x+np.pi/6), label='q-axis')
ax3.legend(loc=5, bbox_to_anchor=(-0.1, 0.5))
ax3.set_title('Park Transformation')

def animate(i):
	# update the data
	theta = i*np.pi/180
	r_line.set_ydata(np.sin(x + theta))
	y_line.set_ydata(np.sin(x - 2*np.pi/3 + theta))
	b_line.set_ydata(np.sin(x - 4*np.pi/3 + theta))

	alpha_line.set_ydata(np.sin(x+theta))
	beta_line.set_ydata(1/(3**0.5)*(np.sin(x+theta)+2*np.sin(x-2*np.pi/3+theta)))
	
	d_line.set_ydata(np.sin(x+theta)*np.cos(x+theta+np.pi/6)+1/(3**0.5)*(np.sin(x+theta)+2*np.sin(x-2*np.pi/3+theta))*np.sin(x+theta+np.pi/6))
	q_line.set_ydata(np.sin(x+theta)*-np.sin(x+theta+np.pi/6)+1/(3**0.5)*(np.sin(x+theta)+2*np.sin(x-2*np.pi/3+theta))*np.cos(x+theta+np.pi/6))
	return r_line, y_line, b_line, alpha_line, beta_line, d_line, q_line,
	

# Init only required for blitting to give a clean slate.
def init():
	r_line.set_ydata(np.ma.array(x, mask=True))
	y_line.set_ydata(np.ma.array(x, mask=True))
	b_line.set_ydata(np.ma.array(x, mask=True))
	
	alpha_line.set_ydata(np.ma.array(x, mask=True))
	alpha_line.set_ydata(np.ma.array(x, mask=True))
	
	d_line.set_ydata(np.ma.array(x, mask=True))
	q_line.set_ydata(np.ma.array(x, mask=True))
	return r_line, y_line, b_line, alpha_line, beta_line, d_line, q_line,

ani = animation.FuncAnimation(fig, animate, 360, init_func=init,
                              interval=10, blit=True)
plt.show()
