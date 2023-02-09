import matplotlib.pyplot as plt
import numpy as np
 
def circle_plotter(radius=10):
    """ Рисует окружность заданного радиуса
    """
    
    x = np.arange(-2*radius, 2*radius, 0.1)
    y = np.arange(-2*radius, 2*radius, 0.1)
    return x, y
    # Переход к неявнозаданным координатам
X, Y = [], []
  # Уравнение окружности

    # Команда рисования
plt.t(X, Y)
plt.title('Эллипс')
plt.grid('equal')
plt.savefig('ellips.png')
    
circle_plotter()


