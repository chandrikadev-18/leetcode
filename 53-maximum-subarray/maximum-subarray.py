class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        best = nums[0]
        ans = nums[0]
        n = len(nums)
        for i in range(1,n):
            v1 = best + nums[i]
            v2 = nums[i]

            best = max(v1,v2)
            ans = max(ans,best)
        return ans