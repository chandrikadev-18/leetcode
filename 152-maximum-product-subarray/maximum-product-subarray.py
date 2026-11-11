class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        minEnding = nums[0]
        maxEnding = nums[0]
        ans = nums[0]
        n = len(nums)
        for i in range(1,n):
            v1 = minEnding * nums[i]
            v2 = maxEnding * nums[i]
            v3 = nums[i]

            minEnding = min(v1,min(v2,v3))
            maxEnding = max(v1,max(v2,v3))

            ans = max(minEnding,max(maxEnding,ans))
        return ans