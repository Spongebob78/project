import matplotlib.pyplot as plt

plt.plot([3, 4], [40, 1], color='g', label='luchte')
plt.xlabel('coord: x')
plt.ylabel('coord: y')
plt.legend()
plt.title('Base')
plt.grid()
plt.savefig('pib.png')