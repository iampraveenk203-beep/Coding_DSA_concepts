"""
Quick Sort: It is also called as Devide and Conquare algorithm.
            It uses pivot element to devide the the array.
            It uses revursion to conquare the the devided list/array to get the sorted array
"""
def quick_sort(arr):
    if len(arr) <= 1 :
        return arr

    # Get the pivot value as last element in list.
    pivot = arr[-1]

    # Extract Left half where values are less than pivot
    Left = [x for x in arr[:-1] if x <= pivot]
    # Extract Right half where values are greater than pivot
    Right = [x for x in arr[:-1] if x >= pivot]

    Left = quick_sort(Left)
    Right = quick_sort(Right)

    # Combine Left list + Pivot element + Right list
    return Left + [pivot] + Right

arrayA = [-2,4,2,-4,1,2,5,7]
print(f"Quick sort is: {quick_sort(arrayA)}")
