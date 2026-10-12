"""
    Bubble Sort: Iterate through the list of numbers and compare the ith and ith - 1 )When i starts with 1, array[i-1] > array[i] then swap the numbers as array[i], array[i+1] = array[i+1], array[i].
    Iterate the list untill no swap needed.
    It changes the list in-place so space complexity: O(1) and time: O(n^2).
"""
def bubble_sort(arr):
    len_arr = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1,len_arr):
            # Check i-1 greater than i, then swap the numbers.
            if arr[i-1] > arr[i]:
                # Set swapped to True so that while continues the loop.
                swapped = True
                arr[i-1], arr[i] = arr[i], arr[i-1]
    return arr
                
arrayA = [-3,2,4,6,-1,8]
print(f"Bubble sort completed: {bubble_sort(arrayA)}")

# OUTPUT:
#Bubble sort completed: [-3, -1, 2, 4, 6, 8]

