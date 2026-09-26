class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        a1 = []
        a2 = []
        for i in nums:
            if i > 0:
                a1.append(i)
            else:
                a2.append(i)
        result = [x*x for x in a1+a2]
        result.sort()
        return result