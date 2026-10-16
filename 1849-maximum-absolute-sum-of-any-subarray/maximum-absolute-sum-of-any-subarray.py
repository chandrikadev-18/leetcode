class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        max_sum = 0
        min_sum = 0

        current_max = 0
        current_min = 0

        for num in nums:
            # Kadane for maximum subarray sum
            current_max = max(num, current_max + num)
            max_sum = max(max_sum, current_max)

            # Kadane for minimum subarray sum
            current_min = min(num, current_min + num)
            min_sum = min(min_sum, current_min)

        return max(max_sum, abs(min_sum))