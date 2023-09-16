# Write  a python code to to move all zeroes at the end of  list/Array

# Input :  [8, 0, 7, 4, 2, 0, 1, 0]  
# Output : [8, 7, 4, 2, 1, 0, 0, 0] 


def move_zeroes_to_end(l1):
    result = []
    count_zeroes = 0
    for i in l1:
        if i != 0:
            result.append(i)
        if i == 0:
            count_zeroes += 1

    result = result + [0] * 3
    print(result)

move_zeroes_to_end([8, 0, 7, 4, 2, 0, 1, 0])
