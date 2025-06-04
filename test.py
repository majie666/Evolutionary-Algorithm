import numpy as np
import matplotlib.pyplot as plt
N_KID = 10
base = N_KID * 2
rank = np.arange(1, base + 1)
util_ = np.maximum(0, np.log(base / 2 + 1) - np.log(rank))
utility = util_ / util_.sum() - 1 / base

plt.plot(utility)
plt.show()
