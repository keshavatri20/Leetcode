class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
            cur,maxi=0,nums[0]
            for i in range(len(nums)):
                    if cur<0:
                        cur=0
                    cur = cur+nums[i]
                    maxi = max(cur,maxi)
            return maxi       