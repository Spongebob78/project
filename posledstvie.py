import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='red', label='Ball')
 
def circle_move(R, k, time):
    R = k * time # линейная 
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = R*np.cos(alpha)
    y = R*np.sin(alpha)
    return x, y
	
edge = 100
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    ball.set_data(circle_move(R=1, k=1, time=i))
    
ani = animation.FuncAnimation(fig,
                              animate,
                              frames=100,
                              interval=90
                             )
 
ani.save('posledstvie.gif')