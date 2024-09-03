#matplotlib: visualizador de dados
#numpy é alimentador de dados

import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.random(50) * 100 #função random gera valores aleatórios entre 0 e 1
y_data = np.random.random(50) * 100

#plt.scatter(x_data , y_data)
#plt.scatter(x_data, y_data, c="black")
plt.scatter(x_data, y_data, c="#000", marker="+", s=150, alpha=0.3) #alpha = transparência

plt.show()