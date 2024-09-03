import numpy as np
import matplotlib.pyplot as plt

# years = [2016 + x for x in range(8)]
# weight = [65, 78, 75, 73,
#           72, 75, 76, 77]

# plt.plot(years, weight, c="b", lw=2, linestyle="--")
# plt.plot(years, weight, "r--", lw=2)

ling = ["Go", "Java", "Python", "C++", "Javascript"]
voting = [3,    6,        15,     40,       35]

plt.bar(ling, voting, color= "c", edgecolor="blue", lw = 2, align = "edge", width=0.3)

plt.show()

