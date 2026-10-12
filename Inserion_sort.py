"""
Insertion Sort: Is simple implementation and efficient for small data.
Space complexity: Inplace O(1)
Time complexisty: O(n^2)
"""
def insertion_sort(arr):
    len_arr = len(arr)
    for i in range(1, len_arr):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                # Break the j loop
                break
    return arr

arrayA = [-5,3,2,1,-3,-3,7,2,2]
print(f"Insertion sort: {insertion_sort(arrayA)}")

#OUTPUT:
#Insertion sort: [-5, -3, -3, 1, 2, 2, 2, 3, 7]