class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()

        new_s = ""

        for ch in s:
            if ch.isalnum():
                new_s += ch

        i = 0
        j = len(new_s) - 1

        while i < j:

            if new_s[i] == new_s[j]:
                i += 1
                j -= 1

            else:
                return False

        return True