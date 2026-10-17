class Solution:
    def sortArrayByParityII(self, nums):
        even = 0
        odd = 1

        while even < len(nums) and odd < len(nums):

            # Find an even number for an even index
            while even < len(nums) and nums[even] % 2 == 0:
                even += 2

            # Find an odd number for an odd index
            while odd < len(nums) and nums[odd] % 2 == 1:
                odd += 2

            # Swap wrong elements
            if even < len(nums) and odd < len(nums):
                nums[even], nums[odd] = nums[odd], nums[even]

        return nums