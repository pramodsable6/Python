def into_to_ip(n):
    first = n % 256
    n = n >> 8
    second = n % 256
    n = n >> 8
    third = n % 256
    n = n >> 8
    fourth = n % 256

    result = [fourth, third, second, first]
    result = [str(i) for i in result]

    return '.'.join(result)

print(into_to_ip(1690900060))
