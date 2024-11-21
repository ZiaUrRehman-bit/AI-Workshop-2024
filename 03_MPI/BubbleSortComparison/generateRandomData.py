import numpy as np

data = np.random.randint(0, 1000000, 10000000)
np.savetxt("hugeData.txt", data, fmt="%d")