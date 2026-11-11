class Solution:
    def maximumSum(self, arr: List[int]) -> int:

        no_delete = arr[0]
        one_delete = 0

        result = arr[0]

        for i in range(1, len(arr)):

            temp = no_delete

            no_delete = max(arr[i], no_delete + arr[i])

            one_delete = max(temp, one_delete + arr[i])

            result = max(result, no_delete, one_delete)

        return result