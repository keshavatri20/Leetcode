class Solution:
    def twoSum(self, nums, target):
        num_dict = {}  # Create a dictionary to store the numbers and their indices
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []  # Return an empty list if no solution is found
