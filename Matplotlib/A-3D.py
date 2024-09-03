import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection="3d")

# x = np.random.random(100)
# y = np.random.random(100)
# z = np.random.random(100)
# ax.scatter(x, y, z)

#Surface plot
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
x, y = np.meshgrid(x, y)
z = np.sin(x) * np.cos(y)
ax.plot_surface(x, y, z, cmap="Spectral")
ax.view_init(azim=0, elev=90)

plt.show()