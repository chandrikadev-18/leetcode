class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        even = 0
        arr_even = []
        arr_odd = []
        while even < len(nums):
            if nums[even] %2 == 0:
                arr_even.append(nums[even])
                even += 1
            else:
                arr_odd.append(nums[even])
                even += 1
        result = arr_even + arr_odd
        return result

        