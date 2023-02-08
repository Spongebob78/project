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

def X(t):
    return R1*np.cos(2*np.pi*t/T1)
def Y(t):
    return R1*np.sin(2*np.pi*t/T1)
def x(t):
    return R2*np.cos(2*np.pi*t/T2)
def y(t):
    return R2*np.sin(2*np.pi*t/T2)

def XVenera(t):
    return R3*np.cos(2*np.pi*t/T1)
def YVenera(t):
    return R3*np.sin(2*np.pi*t/T1)

def Xcometa(t):
    return R1*np.cos(2*np.pi*t/-T1)
def Ycometa(t):
    return R1*np.sin(2*np.pi*t/-T1)

def XMercur(t):
    return R4*np.cos(2*np.pi*t/T1)
def YMercur(t):
    return R4*np.sin(2*np.pi*t/T1)

t=[T1*i/N for i in np.arange(0,N,1)]

X=np.array([X(w) for w in t])
Y=np.array([Y(w) for w in t])
x=np.array([x(w) for w in t])
y=np.array([y(w) for w in t])
XVenera=np.array([XVenera(w) for w in t])
YVenera=np.array([YVenera(w) for w in t])
Xcometa=np.array([Xcometa(w) for w in t])
Ycometa=np.array([Ycometa(w) for w in t])
XMercur=np.array([XMercur(w) for w in t])
YMercur=np.array([YMercur(w) for w in t])

XG = X+x
YG = Y+y

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
    plt.title('Столкновение астероида с планетой Земля')
    ax.set_facecolor('black')
    c=plt.Circle ((0, 0), radius= 0.07*10**8 , color='gold', alpha= .3 )
    plt.gca ().add_artist (c)
    zemly.set_data(X[i], Y[i])
    luna.set_data(XG[i], YG[i])
    venera.set_data(XVenera[i], YVenera[i])
    cometa.set_data(Xcometa[i], Ycometa[i])
    Mercur.set_data(XMercur[i], YMercur[i])
    trajectory2.set_data(XVenera[:i], YVenera[:i])
    trajectory.set_data(X[:i], Y[:i])
    trajectory1.set_data(XG[:i], YG[:i])
    trajectory3.set_data(Xcometa[i], Ycometa[i])
    trajectory4.set_data(XMercur[:i], YMercur[:i])
    
ani = animation.FuncAnimation(fig,
                              animate,
                              frames=500,
                              interval=30,
                             )

ani.save('project_180.gif')