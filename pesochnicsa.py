import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

R1=1.5*10**8
R2 = 1*10**8
T1=3.2*10**7
T2=2.8*10**7
N=1000

def X(t):
    return -R1*np.cos(2*np.pi*t/-T1)
def Y(t):
    return -R1*np.sin(2*np.pi*t/-T1)

t=[T1*i/N for i in np.arange(0,N,1)]

X=np.array([X(w) for w in t])
Y=np.array([Y(w) for w in t])

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='blue')
trajectory, = plt.plot([], [], '-', color='red')

edge = 2*10**8
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    ax.set_facecolor('black')
    c=plt.Circle ((0, 0), radius= 0.3*10**8 , color='red', alpha= .3 )
#add circle to plot (gca means "get current axis")
    plt.gca ().add_artist (c)
    ball.set_data(X[i], Y[i])
    trajectory.set_data(X[i], Y[i])

ani = animation.FuncAnimation(fig,
                              animate,
                              frames=250,
                              interval=30,
                             )

ani.save('2.gif')