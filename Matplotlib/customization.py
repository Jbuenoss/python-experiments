import numpy as np
import matplotlib.pyplot as plt

years = [2015 + x for x in range(10)]       #vai aparecer 10 valores
income = [55, 56, 50, 78, 98,
          100, 112, 124, 124, 151]

income_ticks = list(range(50, 160, 4))       #rótulos do eixo y

plt.plot(years, income)
plt.title("Income of Jonh (in USD)", fontsize=20, fontname="Comic Sans MS")
plt.ylabel("Income in USD")
plt.xlabel("years")
plt.yticks(income_ticks, [f"${x}K" for x in income_ticks])

plt.show()