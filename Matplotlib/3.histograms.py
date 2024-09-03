import numpy as np
import matplotlib.pyplot as plt

#Histograma é usado para dados continuos enquanto o gráfico de barras para por categorias no eixo horizontal

x_data = np.random.normal(40, 1.5, 1000)    #média, desvio padrão, quantidade

print(x_data)
# plt.hist(x_data,
#          edgecolor = "black",
#          lw = 2,
#          bins = 20)

plt.hist(x_data,
         bins = [x_data.min(), 38.5, 41.5, x_data.max()],   #definindo o número de caixas com base numa coleção
         cumulative= True)   


plt.show()