import matplotlib.pyplot as plt

#set axis limits of plot (x=0 to 20, y=0 to 20)
plt.axis([0, 20, 0, 20])
plt.axis ("equal")

#create circle with (x, y) coordinates at (10, 10)
c=plt.Circle ((10, 10), radius= 3 , color='red', alpha= .3 )

#add circle to plot (gca means "get current axis")
plt.gca ().add_artist (c)

plt.savefig('sun.png')