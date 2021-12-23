# Problem: Reverse an array in-place in O(N) linear running time
def reverse(nums):
    
    start_index = 0  # index pointing to the first item
    end_index = len(nums) - 1  # index pointing to the last item
    
    # This algorithm has a linear running time complexity i.e O(N)
    while end_index > start_index:
        # swap the items
        nums[end_index], nums[start_index] = nums[start_index], nums[end_index]
        start_index += 1
        end_index -= 1
    

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]    
    reverse(x)
    print(x)
