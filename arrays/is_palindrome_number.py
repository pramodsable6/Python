def is_palindrome(x):
        reverse = 0
        n = x
        while n > 0:
            reverse = reverse * 10 + n % 10
            n = n // 10
        return reverse == x

print(is_palindrome(121))
# TODO: Time Complexity - O(n) or O(logn) ??
