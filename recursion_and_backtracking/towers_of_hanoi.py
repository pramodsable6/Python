def towers_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        # base case
        print(f'Move disk 1 from rod {source} to rod {destination}')
        return
    towers_of_hanoi(n-1, source, auxiliary, destination)  # Move n-1 disks from source to auxiliary
    print(f'Move disk {n} from rod {source} to rod {destination}')
    towers_of_hanoi(n-1, auxiliary, destination, source)  # Move n-1 disks from auxiliary to destination


towers_of_hanoi(3, 'A', 'C', 'B')

# Time complexity = O(2^n)
# This is a Geometric series with Sum = 2^n - 1
# i.e. number of steps to required to solve the puzzle is 2^n - 1 where n is number of disks
