import numpy as np
import matplotlib.pyplot as plt

languagues = ['go', 'java', 'c++', 'c#', 'elixir', 'python']
vot = [10, 18, 20, 12, 5, 25]
explodes = [0, 0, 0, 0, 0.1, 0]

plt.pie(vot,
        labels= languagues,
        explode= explodes,      #destaque do gráfico
        autopct= "%.2f%%",
        pctdistance= 0.7,
        startangle=90)


# height = np.random.normal(175, 5, 100)
# plt.boxplot(height)



plt.show()
