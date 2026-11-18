class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:

        n = len(nums)
        res = [-1] * n
        st = []

        for i in range(2 * n):

            idx = i % n

            while st and nums[st[-1]] < nums[idx]:
                res[st.pop()] = nums[idx]

            if i < n:
                st.append(idx)

        return res