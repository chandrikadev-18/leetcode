class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        max_freq = 0
        freq = {}

        for right in range(len(s)):
            # Add current character
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Highest frequency character in current window
            max_freq = max(max_freq, freq[s[right]])

            # Number of characters we need to replace
            # = window size - most frequent character
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            # Update answer
            max_len = max(max_len, right - left + 1)

        return max_len