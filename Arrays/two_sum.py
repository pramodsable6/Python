# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(nums)):
            if target - nums[i] in lookup:
                return [lookup[target - nums[i]], i]
            else:
                lookup[nums[i]] = i
