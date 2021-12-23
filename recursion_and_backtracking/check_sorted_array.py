def is_sorted_array(arr, type='asc'):
    if len(arr) == 1:   # base case
        return True
    if type == 'asc':
        return arr[0] <= arr[1] and is_sorted_array(arr[1:], type)
    elif type == 'desc':
        return arr[0] >= arr[1] and is_sorted_array(arr[1:], type)


print(is_sorted_array([1, 2, 3, 4, 5], 'asc'))
print(is_sorted_array([5, 4, 2, 1, -1], 'desc'))
print(is_sorted_array([5, 4, 5, 0, -1], 'desc'))

# Time Complexity: O(n). Space Complexity: O(n) for recursive stack space.
