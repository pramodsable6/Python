# Generate all k-ary(base k) strings with n bits.
def base_k_strings(n, k):
    if n == 0:
        return []
    if n == 1:
        return [str(i) for i in range(k)]
    return [digit + bitstring for digit in base_k_strings(1, k) for bitstring in base_k_strings(n=n-1, k=k)]

print(base_k_strings(n=4, k=2))
