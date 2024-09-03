import numpy as np
import matplotlib.pyplot as plt

x = np.arange(100)
fig, axs = plt.subplots(2,2)

axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title("Sin wave")

axs[1, 0].plot(x, np.cos(x))
axs[1, 0].set_title("cos wave")

axs[1, 1].plot(x, np.sqrt(x))
axs[1, 1].set_title("Square root wave")
axs[1, 1].set_xlabel("values of x")

x2 = np.delete(x, 0)        #para tirar a excessão do log

axs[0, 1].plot(x2, np.log(x2))
axs[0, 1].set_title("log wave")

fig.suptitle("Variations of x")     #pode colocar fig como plt tbm
fig.tight_layout()

plt.savefig("variations_of_x",
            dpi=300,
            transparent=False)