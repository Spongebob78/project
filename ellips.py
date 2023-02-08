import numpy as np
import matplotlib.pyplot as plt

def ellips(p = 10, ee = 0.5):
    
    fi = np.arange(0, np.pi * 9, 0.01)
    
    r = p / (1 + (ee * np.cos(fi)))
    
    x = r * np.cos(fi)
    y = r * np.sin(fi)
    return x, y

X, Y = [], []

edge = 10
plt.xlim(-edge, edge)
plt.ylim(-edge, edge)
plt.plot(X, Y)
plt.title('Эллипс')
plt.savefig('lab_6_dop_2.png')
