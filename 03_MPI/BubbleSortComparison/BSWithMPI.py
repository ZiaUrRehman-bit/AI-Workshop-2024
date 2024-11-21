def bubbleSort(array):
    # get the size of array
    n = len(array)

    # outer loop 
    for i in range(0,n):
        # inner loop
        for j in range(0, n-i-1):
            # if current element greater then adjecnt then swap
            if array[j] > array[j+1]:
                # swap two elements
                array[j], array[j+1] = array[j+1], array[j] 

    return array

from mpi4py import MPI
import numpy as np
import time

# so first of all we make an object of comm_world
comm = MPI.COMM_WORLD

# and we need rank which is unique id of current process and size
rank = comm.Get_rank()
size = comm.Get_size()

# Now we make 0 process a root process and load the random data 


loadedData = np.loadtxt("randomData.txt", dtype=int)

# and now broadcast the data to all processes
loadedData = comm.bcast(loadedData, root=0)

# note time
currentTime = time.time()

# now split the data into chunks 
chunk = np.array_split(loadedData, size)[rank]
localSortedData = bubbleSort(chunk)

'''
np.array_split(data, size):

data: This is the array that contains the numbers to be sorted.
size: This refers to the total number of processes that will work on the data.
np.array_split() is a function in NumPy that splits the array data into size smaller 
arrays (chunks). Each chunk contains a portion of the original data array.
For example, if data has 1000 elements and there are 4 processes (size = 4), 
np.array_split(data, 4) will result in 4 arrays, each containing approximately 250 
elements (the array is split as evenly as possible).

[rank]:

This selects the chunk for the current process.
rank is the rank (or ID) of the current process. In parallel computing, each process
has a unique rank assigned by the MPI framework (ranging from 0 to size-1).
For example, if rank = 2, it selects the third chunk from the split array.
'''
print(f"Local process {rank} done sorting")

# now gather or collect sorted chunk in root process 
sortedData = comm.gather(localSortedData, root=0)

# now once again sort these sorted chunks on root process
if rank == 0:
    finalSorted = []
    for chunks in sortedData:
        finalSorted.extend(chunks)
    
    lastSorted = bubbleSort(finalSorted)

    print(f"First 10 digits {lastSorted[0:10]}")

endTime = time.time()

if rank == 0:
    print(f"Total Time : {endTime-currentTime}")

'''
1. comm.gather(localSortedData, root=0)
comm.gather(): This is an MPI function that gathers data from all processes and collects
 them on the root process (process with rank == 0).

localSortedData: This is the sorted chunk of data from the current process.
root=0: This specifies that the root process is the process with rank == 0. All other
 processes (with ranks 1, 2, etc.) will send their data to the root process.
So, in this line, every process sends its locally sorted chunk (localSortedData) to
 the root process, which collects all the sorted chunks into the sortedData variable.

If you have, say, 4 processes, and each process sorted a chunk of the data, the root 
process will now have all the sorted chunks gathered into a list of lists: sortedData = [sorted_chunk_0, sorted_chunk_1, sorted_chunk_2, sorted_chunk_3].
2. if rank == 0:
The code after this line will be executed only by the root process (rank == 0). The root
 process is the one that gathers all the sorted chunks from other processes.
3. finalSorted = []
finalSorted = [] initializes an empty list that will be used to store all the elements 
from the sorted chunks combined together.
4. for chunks in sortedData:
for chunks in sortedData: iterates over each element (which is a sorted chunk) in the 
sortedData list. Each chunks represents a sorted portion of the data that was gathered from a 
different process.
5. finalSorted.extend(chunks)
extend() is a built-in Python method that adds all the elements from the given iterable 

(in this case, chunks) to the list (finalSorted).
finalSorted.extend(chunks) adds each element in chunks to the end of the finalSorted list.
Key point: Unlike append(), which adds the entire chunks list as a single item, extend() adds 
each element of the chunks list individually to finalSorted.
Example of extend:
python
Copy code
finalSorted = [1, 2, 3]
chunks = [4, 5, 6]
finalSorted.extend(chunks)
print(finalSorted)
Output:

csharp
Copy code
[1, 2, 3, 4, 5, 6]
In your case, the extend() method will add all the sorted chunks to the finalSorted list. So,
 after the loop, finalSorted will contain all the elements from all sorted chunks.
'''