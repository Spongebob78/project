import numpy as np
import matplotlib.pyplot as plt

def ellips(p = 10, ee = 0.5):
    
    fi = np.arange(0, np.pi * 8, 0.01)
    
    r = p / (1 + (ee * np.cos(fi)))
    
    x = r * np.cos(fi)
    y = r * np.sin(fi)
    return x, y

x, y = [], []
    
plt.plot(x, y)
plt.grid()
plt.axis('equal')
plt.savefig('lab_6_dop_2.png')
