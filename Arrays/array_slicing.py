a = 'abcde'
# a = [1, 2, 3, 4, 5]

start = 1
stop = 3
step = 1

print(a[start:stop])            # get items from start to stop - 1
print(a[start:])                # get items from start to the end of list/string
print(a[:stop])                 # get items from the beginning till stop - 1
print(a[:])                     # get a copy of the whole array
print(a[start:stop:step])       # get items from start to stop - 1, increment/decrement by step
print(a[::-1])                  # with step = -1 reversing the array
