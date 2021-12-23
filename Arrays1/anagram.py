# Problem: check if the given lists are anagram or not

def is_anagram(list1, list2):

    list1 = sorted(list1)             # O(NlogN) runtime
    list2 = sorted(list2)             # O(NlogN) runtime

    for i in range(len(list1)):       # O(N) runtime complexity
        if list1[i] != list2[i]:
            return False
        
    return True


if __name__ == "__main__":
    print(is_anagram(['h', 'e', 'a', 'r', 't'], ['e', 'a', 'r', 't', 'h']))


# Overall runtime complexity - O(N) + O(2NlogN) = O(NlogN)
# Ignore constants and comsider most dominant term
