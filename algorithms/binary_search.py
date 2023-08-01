# https://leetcode.com/problems/binary-search/
# O(log(n)) time | O(1) space

def binary_search(nums, target):
  i = 0
  j = len(nums) - 1

  while i <= j:
	m = (i + j) // 2
	if nums[m] == target:
	  return m
	elif nums[m] < target:
	  i = m + 1
	else:
	  j = m - 1
  return -1
