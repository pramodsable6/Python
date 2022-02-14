def fibo(n):
    result = [1, 1]
    for i in range(2, n):
        result.append(result[i-1] + result[i-2])

    return result

# O(n) time | O(n) space

print(fibo(10))
