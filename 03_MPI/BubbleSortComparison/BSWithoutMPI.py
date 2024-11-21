'''
Explanation Step-by-Step
1. Outer Loop (for i in range(n)):

The outer loop ensures the algorithm makes multiple passes through the array.
After each pass, the largest element in the unsorted part of the array "bubbles" to its correct position at the end.

2. Inner Loop (for j in range(0, n - i - 1)):

The inner loop compares adjacent elements in the array.
n - i - 1 ensures that the already sorted elements at the end are not checked again.

3. Condition (if arr[j] > arr[j + 1]):

This checks if the current element is greater than the next element.
If true, they are swapped to maintain ascending order.

4. Swapping (arr[j], arr[j + 1] = arr[j + 1], arr[j]):

Python’s multiple assignment syntax is used to swap the elements in one line.

5. Return Statement:

After all passes, the array is fully sorted and returned.
'''
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

# in order to check the function we need to generate a large pool of random integer
# we need numpy and time to track the time also we need to save these valuse in .txt file and then load for
# this example and also with MPI
import numpy as np
import time

n = 10000 # may be we ned 1000 random numbers from 0 to 1000
data = np.random.randint(0, 10000, n)

# save the data in .txt file 
np.savetxt("randomData.txt",data, fmt='%d')

# now load data
loadedData = np.loadtxt("randomData.txt", dtype=int)
# we can display the first 10 digits of loaded data
print(f"Lodaded Data: {loadedData[0:10]}")

# now pass this loaded data array to function we have created
# and also note down the current time 
currentTime = time.time()
sortedData = bubbleSort(loadedData)
endTime = time.time()

# now print the details and sorted data first 10 elements and time 
print(f"First 10 digits of Sorted Data: {sortedData[0:10]}")
print(f"Total Time Taken: {endTime - currentTime}")