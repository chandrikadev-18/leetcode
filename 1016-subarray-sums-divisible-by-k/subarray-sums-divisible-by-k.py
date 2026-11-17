class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        prefix_sum = 0
        count = 0

        remainder_map = {0: 1}

        for num in nums:

            prefix_sum += num

            remainder = prefix_sum % k

            if remainder in remainder_map:
                count += remainder_map[remainder]

            remainder_map[remainder] = remainder_map.get(remainder, 0) + 1

        return count