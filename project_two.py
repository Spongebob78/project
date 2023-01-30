import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

R1=1.496*10**8
T1=3.156*10**7
R2=3.844*10**7
T2=2.36*10**6
N=1000.0
RVenera = 1.2*10**8

def X(t):
    return R1*np.cos(2*np.pi*t/T1)
def Y(t):
    return R1*np.sin(2*np.pi*t/T1)
def x(t):
    return R2*np.cos(2*np.pi*t/T2)
def y(t):
    return R2*np.sin(2*np.pi*t/T2)

def XVenera(t):
    return RVenera*np.cos(2*np.pi*t/T1)
def YVenera(t):
    return RVenera*np.sin(2*np.pi*t/T1)

t=[T1*i/N for i in np.arange(0,N,1)]

X=np.array([X(w) for w in t])
Y=np.array([Y(w) for w in t])
x=np.array([x(w) for w in t])
y=np.array([y(w) for w in t])

XG = X+x
YG = Y+y

fig, ax = plt.subplots()
zemly, = plt.plot([], [], 'o', color='blue')
luna, = plt.plot([], [], 'o', color='gray')
trajectory, = plt.plot([], [], '-', color='blue')
trajectory1, = plt.plot([], [], '-', color='blue')


edge = 2*10**8
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    plt.plot([0], [0] , marker='o', color='gold')
    zemly.set_data(X[i], Y[i])
    luna.set_data(XG[i], YG[i])
    trajectory.set_data(X[:i], Y[:i])
    trajectory1.set_data(XG[:i], YG[:i])
    
    
ani = animation.FuncAnimation(fig,
                              animate,
                              frames=1000,
                              interval=30,
                             )

ani.save('trajectory_zemly_and_luna.gif')