 """
 Selection sort:
      Find the minimum value in the list.
      Swalp it with the value in current position.
      Repeat untill the list is sorted.
      Space: O(1)
      Time: O(n^2)
 This algorithm called selection sort because it repeatedly selects the smallest element.
 """

def selection_sort(arr):
    len_arr = len(arr)
    for i in range(len_arr):
        min_index = i
        for j in range(i+1, len_arr):
            # Nested loop to check min value from i+1 to n.
            if arr[j] < arr[min_index]:
                # Found the min value index and update min_index from i to j.
                min_index = j
        # Swap the min_index value with current postion i.
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arrayA = [-3,-4,-3,4,2,0,3,6]
print(f"Selection sort: {selection_sort(arrayA)}")

#OUTPUT:
#Selection sort: [-4, -3, -3, 0, 2, 3, 4, 6]