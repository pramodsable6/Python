def contains_common_item(arr1, arr2):
    set1 = set()
    for i in arr1:                              # O(a)
        if i not in set1:                       # O(1)
            set1.add(i)                         # O(1)
    
    for j in arr2:                              # O(b)
        if j in set1:                           # O(1)
            print('True')
        else:
            print('False')

contains_common_item([1, 2, 3, 4, 5], [9, 6, 7, 8, 5])

# Hence time complexity of contains_common_item() is O(a + b), by neglecting the constants rule
# and its Space Complexity is O(a), since we are creating a new set variable
