"""
Merge Sort:
    Devide and Conquare Algorithm: "Devide the given array/list by 2.
    Devide: The unsorted array is repeatedly divided into two roughly equal halves until each subarray contains exactly one element(an array of size 1 is inherently sorted).
    Conquer: The individual subarrays are sorted recursively.
    Merge: The sorted subarrays are merged back together in an orderly fashion.
"""
def mergeSort(arr):
    # Case 1: when arr is with one element
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    lefthalf = arr[:mid]
    righthalf = arr[mid:]

    sorted_left = mergeSort(lefthalf)
    sorted_right = mergeSort(righthalf)

    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i=j=0

    # Compare the single item left and right lists to get the sorted values.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arrayA=[3,7,6,-10,15,23.5,-13]
print(f"Merge sort is: {mergeSort(arrayA)}")

#OUTPUT:
#Merge sort is: [-13, -10, 3, 6, 7, 15, 23.5]