import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")
style.use("dark_background")

eixox = [2017 + x for x in range(6)]
peso1 = [79, 81, 78, 67, 70, 74]
peso2 = [100, 102, 105, 99, 97, 107]
peso3 = [65, 78, 63, 62, 55, 52]
plt.plot(eixox, peso1, label="Peso do Matheus")
plt.plot(eixox, peso2, label="Peso do Bueno")
plt.plot(eixox, peso3, label="Peso do Bruno")     #o eixo x será adicionado automaticamente
plt.legend(loc="lower center")

# languages = ['go', 'java', 'c++', 'c#', 'elixir', 'python']
# vot = [10, 18, 20, 12, 5, 25]
# plt.pie(vot, labels=None)
# plt.legend(labels=languages, loc="upper right")



plt.show()