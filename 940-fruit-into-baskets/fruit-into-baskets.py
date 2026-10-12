class Solution:
    def totalFruit(self, fruits):
        low = 0
        high = 0
        count = {}
        max_fruits = 0

        while high < len(fruits):

            count[fruits[high]] = count.get(fruits[high], 0) + 1

            # Sirf 2 types allowed hain
            while len(count) > 2:
                count[fruits[low]] -= 1

                if count[fruits[low]] == 0:
                    del count[fruits[low]]

                low += 1

            # Window ki length
            max_fruits = max(max_fruits, high - low + 1)

            high += 1

        return max_fruits
        