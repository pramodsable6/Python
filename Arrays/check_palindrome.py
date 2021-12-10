# Problem: check if the given dataing is palindrome or not

def reverse(data):
    
    data = list(data)
    start_index = 0  # index pointing to the first item
    end_index = len(data) - 1  # index pointing to the last item
    
    # This algorithm has a linear running time complexity - O(N)
    while end_index > start_index:
        # swap the items
        data[end_index], data[start_index] = data[start_index], data[end_index]
        start_index += 1
        end_index -= 1

    return ''.join(data)

def is_palindrome(input_string):
    if input_string == reverse(input_string):
        return True
    return False


if __name__ == "__main__":
    print(is_palindrome('madam'))
