class Solution:
    def longestOnes(self, nums, k):
        low = 0
        high = 0
        zero_count = 0
        max_length = 0

        while high < len(nums):

            # Agar current element 0 hai
            if nums[high] == 0:
                zero_count += 1

            # Agar zeros k se jyada ho gaye
            while zero_count > k:
                if nums[low] == 0:
                    zero_count -= 1

                low += 1

            # Valid window ki maximum length
            max_length = max(max_length, high - low + 1)

            high += 1

        return max_length