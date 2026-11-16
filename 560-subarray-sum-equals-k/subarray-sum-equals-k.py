class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        mp = {0: 1}
        prefix = 0
        ans = 0

        for num in nums:

            prefix += num

            rem = prefix - k

            if rem in mp:
                ans += mp[rem]

            mp[prefix] = mp.get(prefix, 0) + 1

        return ans
             