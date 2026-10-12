"""
Count Sort: This is algorith where we do not compare the elements in the list/array (non-comparision).
            it sort the array using frequency array/list.
            1. Get the list/array
            2. Get the maximum number of the array
            3. Create the freq array with lenght of (max_number + 1)
            4. Store the freq array values with count of each element
            5. Generate the sorted_arr using freq array
"""
def count_sort(arr):
    # Case 1: Empty array
    if not arr:
        return arr

    # Case 2: Find the max value in original array
    max_val = max(arr)

    # Case 3: Create freq array
    count = [0] * (max_val + 1)

    # Case 4: Update freq array based on original array
    for num in arr:
        count[num] += 1

    sorted_arr = []

    # Case 5: Create the sorted array
    for val, freq in enumerate(count):
        sorted_arr.extend([val] * freq)

    return sorted_arr

print(f"Count sort is: {count_sort([1,2,5,2,3,1,3,6,8,2])}")