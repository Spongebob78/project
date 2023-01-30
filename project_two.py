import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

R1=1.496*10**8
T1=3.156*10**7
R2=3.844*10**7
T2=2.36*10**6
N=1000.0
R3 = 1*10**8

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

t=[T1*i/N for i in np.arange(0,N,1)]

X=np.array([X(w) for w in t])
Y=np.array([Y(w) for w in t])
x=np.array([x(w) for w in t])
y=np.array([y(w) for w in t])
XVenera = np.array([XVenera(w) for w in t])
YVenera = np.array([YVenera(w) for w in t])

XG = X+x
YG = Y+y

fig, ax = plt.subplots()
zemly, = plt.plot([], [], 'o', color='blue')
luna, = plt.plot([], [], 'o', color='gray')
venera, = plt.plot([], [], 'o', color='red')
trajectory, = plt.plot([], [], '-', color='blue')
trajectory1, = plt.plot([], [], '-', color='gray')
trajectory2, = plt.plot([], [], '-', color='red')

edge = 2*10**8
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    plt.plot([0], [0] , marker='o', color='gold')
    zemly.set_data(X[i], Y[i])
    luna.set_data(XG[i], YG[i])
    venera.set_data(XG[i], YG[i])
    trajectory2.set_data(XVenera[:i], YVenera[:i])
    trajectory.set_data(X[:i], Y[:i])
    trajectory1.set_data(XG[:i], YG[:i])
    
    
ani = animation.FuncAnimation(fig,
                              animate,
                              frames=300,
                              interval=30,
                             )

ani.save('trajectory_zemly_and_luna.gif')