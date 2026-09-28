class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        x, y, z = target

        a = b = c = 0

        for t in triplets:
            # Target se koi bhi value badi hai to ye triplet use nahi kar sakte
            if t[0] <= x and t[1] <= y and t[2] <= z:
                a = max(a, t[0])
                b = max(b, t[1])
                c = max(c, t[2])

        return [a, b, c] == target