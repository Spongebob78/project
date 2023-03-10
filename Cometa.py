import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Cursor

R1=1.496*10**8
T1=3.156*10**7
R2=3.844*10**7
T2=2.36*10**6
N=1000.0
R3 = 0.86*10**8
R4 = 0.4*10**8

def Xcometa(t):
    return R1*np.cos(2*np.pi*t/-T1)
def Ycometa(t):
    return R1*np.sin(2*np.pi*t/-T1)

t=[T1*i/N for i in np.arange(0,N,1)]

Xcometa=np.array([Xcometa(w) for w in t])
Ycometa=np.array([Ycometa(w) for w in t])

fig, ax = plt.subplots()
zemly, = plt.plot([], [], 'o', color='darkgreen')
luna, = plt.plot([], [], 'o', color='gray')
venera, = plt.plot([], [], 'o', color='orange')
cometa, = plt.plot([], [], '.', color='red')
Mercur, = plt.plot([], [], 'o', color='firebrick')
trajectory, = plt.plot([], [], '-', color='blue')
trajectory1, = plt.plot([], [], '-', color='gainsboro')
trajectory2, = plt.plot([], [], '-', color='y')
trajectory3, = plt.plot([], [], '-', color='red')
trajectory4, = plt.plot([], [], '-', color='red')

edge = 2*10**8
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    plt.title('Астероид')
    cometa.set_data(Xcometa[i], Ycometa[i])
    trajectory3.set_data(Xcometa[i], Ycometa[i])
    
ani = animation.FuncAnimation(fig,
                              animate,
                              frames=900,
                              interval=30,
                             )

ani.save('Cometa.gif')