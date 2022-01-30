# O(2^n) time | O(n) space
# Time complexity is O(2^n) because we are making two additional function calls on every call.

def getNthFib(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	
	return getNthFib(n-1) + getNthFib(n-2)
