
def simplePythonSort(array):
    return sorted(array)


import numpy as np
import time

loadedData = np.loadtxt("hugeData.txt", dtype=int)

currentTime = time.time()
sortedData = simplePythonSort(loadedData)
endTime = time.time()

print(f"First 10 sorted digits: {sortedData[0:10]}, and time taken {endTime - currentTime}")
