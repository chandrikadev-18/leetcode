class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        maxEnding = nums[0]
        minEnding = nums[0]
        maxans = nums[0]
        minans = nums[0]
        sum = nums[0]
        for i in range(1,len(nums)):
            sum = sum + nums[i]
            v1 = maxEnding + nums[i]
            v2 = minEnding + nums[i]
            v3 = nums[i]

            maxEnding = max(v1,v3)
            minEnding = min(v2,v3)

            maxans = max(maxans,maxEnding)
            minans = min(minans,minEnding)

        if maxans < 0:
            return maxans

        a2 = sum - minans
        res = max(maxans,a2)

        return res