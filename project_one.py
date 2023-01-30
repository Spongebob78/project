import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Cursor

R1=1.5*10**8
R2 = 1*10**8
T1=3.2*10**7
T2=2.8*10**7
N=1000

def X(t):
    return R1*np.cos(2*np.pi*t/T1)
def Y(t):
    return R1*np.sin(2*np.pi*t/T1)
def Xx(t):
    return R2*np.cos(2*np.pi*t/T2)
def Yy(t):
    return R2*np.sin(2*np.pi*t/T2)
def Xcometa(t):
    return -R1*np.cos(2*np.pi*t/-T1)
def Ycometa(t):
    return -R1*np.sin(2*np.pi*t/-T1)


t=[T1*i/N for i in np.arange(0,N,1)]

X=np.array([X(w) for w in t])
Y=np.array([Y(w) for w in t])
Xx=np.array([Xx(w) for w in t])
Yy=np.array([Yy(w) for w in t])
Xcometa=np.array([Xcometa(w) for w in t])
Ycometa=np.array([Ycometa(w) for w in t])


fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='blue')
ball1, = plt.plot([], [], 'o', color='red')
ball2, = plt.plot([], [], '.', color='red')
trajectory, = plt.plot([], [], '-', color='red')
trajectory1, = plt.plot([], [], '-', color='red')
trajectory2, = plt.plot([], [], '-', color='red')

edge = 2*10**8
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):


    c=plt.Circle ((0,0), radius= 20 , color='gold')
    plt.gca ().add_artist (c)
    ball.set_data(X[i], Y[i])
    ball1.set_data(Xx[i], Yy[i])
    ball2.set_data(Xcometa[i], Ycometa[i])
    trajectory.set_data(X[i], Y[i])
    trajectory1.set_data(Xx[i], Yy[i])
    trajectory2.set_data(Xcometa[i], Ycometa[i])

ani = animation.FuncAnimation(fig,
                              animate,
                              frames=200,
                              interval=30,
                             )

ani.save('1.gif')