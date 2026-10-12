"""
Priority Queue is Abstract Data Type (ADT OR Interface).
For the implementation we use heapq as concrete data structure used.

Python provides the heapq module to implement Heap (Default: Min-Heap).

Min-Heap: Value of the parent node is always less than or equal of its children.
Max-Heap: Value of the parent node is always greater or equal of its children.
"""

import heapq

# Binary Tree
A = [2, 5, 0, 1, 10, 8, -4, 3, 12, 9]

# Convert the A to Heap Binary Tree (Min Heap bydefault)
heapq.heapify(A)
print(f"Converted to Heap using heapify: {A}")

#Heap Push (Insert item)
heapq.heappush(A, 4)

# Heap Pop (Extract Min)
extract_min = heapq.heappop(A)
print(f"Extracted min: {extract_min}")


# Heap Sort (Default to Min Heap)
def heapsort(numbers):
    heapq.heapify(numbers # Always going to create min-heap
    n = len(numbers)
    sorted_list = [0] * n
    for i in range(n):
        minn = heapq.heappop(numbers)
        sorted_list[i] = minn
    return sorted_list

print(f"Sorted list is: {heapsort([1,2,2,5,3,5,2,8,5])}")

#OUTPUT
#Sorted list is: [1, 2, 2, 2, 3, 5, 5, 5, 8]

# This method push item and extract the min item at same time
print(f"heappushpop: {heapq.heappushpop(A, 20)}")

# MAX-HEAP behaviour by negating the numbers in the list.

# Write code to create Max-heap with the given list.
B = [-4,3,1,0,2,5,10,8,12,9]

# Get the length of the list
n = len(B)

# Traverse the list and convert the number to its negative.
for i in range(n):
    B[i] = -B[i]
    
# Convert to heap using heapify
heapq.heapify(B) # [-12,-9,-10,-8,-2,-5,-1,-3,0,4]

# Extract the max from Maxheap by using heappop by converting to negative to positive.
max_extract = -heapq.heappop(B)
print(f"Extracted max: {max_extract}")

# Push item to max heap using negating the number, Ex: If item is 10 then negate that to -10.
heapq.heappush(B, -10) # This pushes 10 to the heap.

# Get the peak item of the heap
print(f"Peak item in the heap A is: {A[0]}")

# Putting the tuples in to heap using hashmap
from collections import Counter
D = [2,3,5,3,2,1,5,6,3,5]
counter = Counter(D)

# Empty Heap
heap = []

for k,v in counter.items():
    heapq.heappush(heap, (v,k))

print(f"Heap created for tuple values: {heap}")

#OUTPUT
#Heap created for tuple values: [(1, 1), (1, 6), (3, 5), (3, 3), (2, 2)]
