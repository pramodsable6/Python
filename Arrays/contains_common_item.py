# Check if two arrays have a common item

# Time Complexity O(a * b) and Space complexity O(1)
def contains_common_item(arr1, arr2):
    for i in arr1:
        for j in arr2:
            if i == j:
                print('True')
                return
    print('False')


# Faster solution O(a + b), but Space complexity = O(a) will consume more memory
def contains_common_item2(arr1, arr2):
    set1 = set()
    for i in arr1:                              # O(a)
        if i not in set1:                       # O(1)
            set1.add(i)                         # O(1)
    
    for j in arr2:                              # O(b)
        if j in set1:                           # O(1)
            print('True')
            return
    print('False')                              # Hence, O(a + b)


# contains_common_item([1, 2, 3, 4, 5], [9, 6, 7, 5, 4])
contains_common_item2([1, 2, 3, 4, 5], [9, 1, 7, 99, 88])
